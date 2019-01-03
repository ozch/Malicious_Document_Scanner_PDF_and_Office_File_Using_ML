
#!/usr/bin/env python
#MADE CHANGES HERE START ######################################################################################
#these are some get and set method and globel function
#which are very crucial to the execution of this service
import oledump as olex
import socket
dir_name = ""

def setDirName(name):
    global dir_name
    dir_name=name

def getDirName():
    return dir_name
def setStringNull():
    global st_ring
    st_ring = ""

st_ring = ""
pic = ""

#MADE CHANGES HERE END ######################################################################################
__description__ = 'OLE DUMP ANALYZER)'
__author__ = 'BU_ISB'
__version__ = '0.0.35'
__date__ = '2018/07/01'


import optparse
import sys
import math
import os
import zipfile
import cStringIO
import binascii
import xml.dom.minidom
import zlib
import hashlib
import textwrap
import re
import string
import codecs
import json
import subprocess
from exchanger import *
ex = Exchanger()

if sys.version_info[0] >= 3:
    from io import StringIO
else:
    from cStringIO import StringIO

try:
    import dslsimulationdb
except:
    dslsimulationdb = None

try:
    import yara
except:
    pass

try:
    import olefile
except:
    print('This program requires module olefile.\nhttp://www.decalage.info/python/olefileio\n')
    if sys.version >= '2.7.9':
        print("You can use PIP to install olefile like this: pip install olefile\npip is located in Python's Scripts folder.\n")
    exit(-1)

dumplinelength = 16
MALWARE_PASSWORD = 'infected'
OLEFILE_MAGIC = '\xD0\xCF\x11\xE0'
ACTIVEMIME_MAGIC = 'ActiveMime'
REGEX_STANDARD = '[\x09\x20-\x7E]'

def PrintManual():
    manual = '''
Manual:
Doesn't Exit
'''
    for line in manual.split('\n'):
        print(textwrap.fill(line))

#Convert 2 Bytes If Python 3
def C2BIP3(string):
    if sys.version_info[0] > 2:
        return bytes([ord(x) for x in string])
    else:
        return string

# CIC: Call If Callable
def CIC(expression):
    if callable(expression):
        return expression()
    else:
        return expression

# IFF: IF Function
def IFF(expression, valueTrue, valueFalse):
    if expression:
        return CIC(valueTrue)
    else:
        return CIC(valueFalse)

def File2String(filename):
    try:
        f = open(filename, 'rb')
    except:
        return None
    try:
        return f.read()
    except:
        return None
    finally:
        f.close()

class cDump():
    def __init__(self, data, prefix='', offset=0, dumplinelength=16):
        self.data = data
        self.prefix = prefix
        self.offset = offset
        self.dumplinelength = dumplinelength

    def HexDump(self):
        oDumpStream = self.cDumpStream(self.prefix)
        hexDump = ''
        for i, b in enumerate(self.data):
            if i % self.dumplinelength == 0 and hexDump != '':
                oDumpStream.Addline(hexDump)
                hexDump = ''
            hexDump += IFF(hexDump == '', '', ' ') + '%02X' % self.C2IIP2(b)
        oDumpStream.Addline(hexDump)
        return oDumpStream.Content()

    def CombineHexAscii(self, hexDump, asciiDump):
        if hexDump == '':
            return ''
        countSpaces = 3 * (self.dumplinelength - len(asciiDump))
        if len(asciiDump) <= self.dumplinelength / 2:
            countSpaces += 1
        return hexDump + '  ' + (' ' * countSpaces) + asciiDump

    def HexAsciiDump(self):
        oDumpStream = self.cDumpStream(self.prefix)
        hexDump = ''
        asciiDump = ''
        for i, b in enumerate(self.data):
            b = self.C2IIP2(b)
            if i % self.dumplinelength == 0:
                if hexDump != '':
                    oDumpStream.Addline(self.CombineHexAscii(hexDump, asciiDump))
                hexDump = '%08X:' % (i + self.offset)
                asciiDump = ''
            if i % self.dumplinelength == self.dumplinelength / 2:
                hexDump += ' '
            hexDump += ' %02X' % b
            asciiDump += IFF(b >= 32 and b <= 128, chr(b), '.')
        oDumpStream.Addline(self.CombineHexAscii(hexDump, asciiDump))
        return oDumpStream.Content()

    def Base64Dump(self, nowhitespace=False):
        encoded = binascii.b2a_base64(self.data)
        if nowhitespace:
            return encoded
        oDumpStream = self.cDumpStream(self.prefix)
        length = 64
        for i in range(0, len(encoded), length):
            oDumpStream.Addline(encoded[0+i:length+i])
        return oDumpStream.Content()

    class cDumpStream():
        def __init__(self, prefix=''):
            self.oStringIO = StringIO()
            self.prefix = prefix

        def Addline(self, line):
            if line != '':
                self.oStringIO.write(self.prefix + line + '\n')

        def Content(self):
            return self.oStringIO.getvalue()

    @staticmethod
    def C2IIP2(data):
        if sys.version_info[0] > 2:
            return data
        else:
            return ord(data)

def HexDump(data):
    return cDump(data, dumplinelength=dumplinelength).HexDump()

def HexAsciiDump(data):
    return cDump(data, dumplinelength=dumplinelength).HexAsciiDump()

def Translate(expression):
    try:
        codecs.lookup(expression)
        command = '.decode("%s")' % expression
    except LookupError:
        command = expression
    return lambda x: eval('x' + command)

def ExtractStringsASCII(data):
    regex = REGEX_STANDARD + '{%d,}'
    return re.findall(regex % 4, data)

def ExtractStringsUNICODE(data):
    regex = '((' + REGEX_STANDARD + '\x00){%d,})'
    return [foundunicodestring.replace('\x00', '') for foundunicodestring, dummy in re.findall(regex % 4, data)]

def ExtractStrings(data):
    return ExtractStringsASCII(data) + ExtractStringsUNICODE(data)

def DumpFunctionStrings(data):
    return ''.join([extractedstring + '\n' for extractedstring in ExtractStrings(data)])

#Fix for http://bugs.python.org/issue11395
def StdoutWriteChunked(data):
    while data != '':
        sys.stdout.write(data[0:10000])
        try:
            sys.stdout.flush()
        except IOError:
            return
        data = data[10000:]
def PrintableNameC(fname, orphan=0):
    if orphan == 1:
        return 'Orphan: ' + repr(fname)
    else:
        return repr('.'.join(fname))

def PrintableName(fname, orphan=0):
    if orphan == 1:
        return 'Orphan: ' + repr(fname)
    else:
        return repr('/'.join(fname))

def ParseTokenSequence(data):
    flags = ord(data[0])
    data = data[1:]
    result = []
    for mask in [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]:
        if len(data) > 0:
            if flags & mask:
                result.append(data[0:2])
                data = data[2:]
            else:
                result.append(data[0])
                data = data[1:]
    return result, data

def OffsetBits(data):
    numberOfBits = int(math.ceil(math.log(len(data), 2)))
    if numberOfBits < 4:
        numberOfBits = 4
    elif numberOfBits > 12:
        numberOfBits = 12
    return numberOfBits

def Bin(number):
    result = bin(number)[2:]
    while len(result) < 16:
        result = '0' + result
    return result

def DecompressChunk(compressedChunk):
    if len(compressedChunk) < 2:
        return None, None
    header = ord(compressedChunk[0]) + ord(compressedChunk[1]) * 0x100
    size = (header & 0x0FFF) + 3
    flagCompressed = header & 0x8000
    data = compressedChunk[2:2 + size - 2]

    if flagCompressed == 0:
        return data, compressedChunk[size:]

    decompressedChunk = ''
    while len(data) != 0:
        tokens, data = ParseTokenSequence(data)
        for token in tokens:
            if len(token) == 1:
                decompressedChunk += token
            else:
                if decompressedChunk == '':
                    return None, None
                numberOfOffsetBits = OffsetBits(decompressedChunk)
                copyToken = ord(token[0]) + ord(token[1]) * 0x100
                offset = 1 + (copyToken >> (16 - numberOfOffsetBits))
                length = 3 + (((copyToken << numberOfOffsetBits) & 0xFFFF) >> numberOfOffsetBits)
                copy = decompressedChunk[-offset:]
                copy = copy[0:length]
                lengthCopy = len(copy)
                while length > lengthCopy: #a#
                    if length - lengthCopy >= lengthCopy:
                        copy += copy[0:lengthCopy]
                        length -= lengthCopy
                    else:
                        copy += copy[0:length - lengthCopy]
                        length -= length - lengthCopy
                decompressedChunk += copy
    return decompressedChunk, compressedChunk[size:]

def Decompress(compressedData):
    if compressedData[0] != chr(1):
        return (False, None)
    remainder = compressedData[1:]
    decompressed = ''
    while len(remainder) != 0:
        decompressedChunk, remainder = DecompressChunk(remainder)
        if decompressedChunk == None:
            return (False, decompressed)
        decompressed += decompressedChunk
    return (True, decompressed.replace('\r\n', '\n'))

def FindCompression(data):
    return data.find('\x00Attribut\x00e ')

def SearchAndDecompressSub(data):
    position = FindCompression(data)
    if position == -1:
        return (False, '')
    else:
        compressedData = data[position - 3:]
    return Decompress(compressedData)

def SearchAndDecompress(data, ifError='Error: unable to decompress\n'):
    result, decompress = SearchAndDecompressSub(data)
    if result:
        return decompress
    elif ifError == None:
        return decompress
    else:
        return ifError

def ReadWORD(data):
    if len(data) < 2:
        return None, None
    return ord(data[0]) + ord(data[1]) *0x100, data[2:]

def ReadDWORD(data):
    if len(data) < 4:
        return None, None
    return ord(data[0]) + ord(data[1]) *0x100 + ord(data[2]) *0x10000 + ord(data[3]) *0x1000000, data[4:]

def ReadNullTerminatedString(data):
    position = data.find('\x00')
    if position == -1:
        return None, None
    return data[:position], data[position + 1:]

def ExtractOle10Native(data):
    size, data = ReadDWORD(data)
    if size == None:
        return []
    dummy, data = ReadWORD(data)
    if dummy == None:
        return []
    filename, data = ReadNullTerminatedString(data)
    if filename == None:
        return []
    pathname, data = ReadNullTerminatedString(data)
    if pathname == None:
        return []
    dummy, data = ReadDWORD(data)
    if dummy == None:
        return []
    dummy, data = ReadDWORD(data)
    if dummy == None:
        return []
    temppathname, data = ReadNullTerminatedString(data)
    if temppathname == None:
        return []
    sizeEmbedded, data = ReadDWORD(data)
    if sizeEmbedded == None:
        return []
    if len(data) < sizeEmbedded:
        return []

    return [filename, pathname, temppathname, data[:sizeEmbedded]]

def Extract(data):
    result = ExtractOle10Native(data)
    if result == []:
        return 'Error: extraction failed'
    return result[3]

def GenerateMAGIC(data):
    return binascii.b2a_hex(data) + ' ' + ''.join([IFF(ord(c) >= 32, c, '.') for c in data])

def Info(data):
    result = ExtractOle10Native(data)
    if result == []:
        return 'Error: extraction failed'
    return 'String 1: %s\nString 2: %s\nString 3: %s\nSize embedded file: %d\nMD5 embedded file: %s\nMAGIC:  %s\nHeader: %s\n' % (result[0], result[1], result[2], len(result[3]), hashlib.md5(result[3]).hexdigest(), GenerateMAGIC(result[3][0:4]), GenerateMAGIC(result[3][0:16]))

def IfWIN32SetBinary(io):
    if sys.platform == 'win32':
        import msvcrt
        msvcrt.setmode(io.fileno(), os.O_BINARY)

def File2Strings(filename):
    try:
        f = open(filename, 'r')
    except:
        return None
    try:
        return map(lambda line:line.rstrip('\n'), f.readlines())
    except:
        return None
    finally:
        f.close()

def ProcessAt(argument):
    if argument.startswith('@'):
        strings = File2Strings(argument[1:])
        if strings == None:
            raise Exception('Error reading %s' % argument)
        else:
            return strings
    else:
        return [argument]

def AddPlugin(cClass):
    global plugins

    plugins.append(cClass)
#Something wrong here dont
#def ExpandFilenameArguments(filenames):
#    return list(collections.OrderedDict.fromkeys(sum(map(glob.glob, sum(map(ProcessAt, filenames), [])), [])))

class cPluginParent():
    macroOnly = False
    indexQuiet = False

def LoadPlugins(plugins, plugindir, verbose):
    if plugins == '':
        return

    if plugindir == '':
        scriptPath = os.path.dirname(sys.argv[0])
    else:
        scriptPath = plugindir

    for plugin in sum(map(ProcessAt, plugins.split(',')), []):
        try:
            if not plugin.lower().endswith('.py'):
                plugin += '.py'
            if os.path.dirname(plugin) == '':
                if not os.path.exists(plugin):
                    scriptPlugin = os.path.join(scriptPath, plugin)
                    if os.path.exists(scriptPlugin):
                        plugin = scriptPlugin
            exec open(plugin, 'r') in globals(), globals()
        except Exception as e:
            print('Error loading plugin: %s' % plugin)
            if verbose:
                raise e

def AddDecoder(cClass):
    global decoders

    decoders.append(cClass)

class cDecoderParent():
    pass

def LoadDecoders(decoders, decoderdir, verbose):
    if decoders == '':
        return

    if decoderdir == '':
        scriptPath = os.path.dirname(sys.argv[0])
    else:
        scriptPath = decoderdir

    for decoder in sum(map(ProcessAt, decoders.split(',')), []):
        try:
            if not decoder.lower().endswith('.py'):
                decoder += '.py'
            if os.path.dirname(decoder) == '':
                if not os.path.exists(decoder):
                    scriptDecoder = os.path.join(scriptPath, decoder)
                    if os.path.exists(scriptDecoder):
                        decoder = scriptDecoder
            exec open(decoder, 'r') in globals(), globals()
        except Exception as e:
            print('Error loading decoder: %s' % decoder)
            if verbose:
                raise e

class cIdentity(cDecoderParent):
    name = 'Identity function decoder'

    def __init__(self, stream, options):
        self.stream = stream
        self.options = options
        self.available = True

    def Available(self):
        return self.available

    def Decode(self):
        self.available = False
        return self.stream

    def Name(self):
        return ''

def DecodeFunction(decoders, options, stream):
    if decoders == []:
        return stream
    return decoders[0](stream, options.decoderoptions).Decode()

def MacrosContainsOnlyAttributesOrOptions(stream):
    lines = SearchAndDecompress(stream).split('\n')
    for line in [line.strip() for line in lines]:
        if line != '' and not line.startswith('Attribute ') and not line == 'Option Explicit':
            return False
    return True

#https://msdn.microsoft.com/en-us/library/windows/desktop/dd317756%28v=vs.85%29.aspx
dCodepages = {
    037: 'IBM EBCDIC US-Canada',
    437: 'OEM United States',
    500: 'IBM EBCDIC International',
    708: 'Arabic (ASMO 708)',
    709: 'Arabic (ASMO-449+, BCON V4)',
    710: 'Arabic - Transparent Arabic',
    720: 'Arabic (Transparent ASMO); Arabic (DOS)',
    737: 'OEM Greek (formerly 437G); Greek (DOS)',
    775: 'OEM Baltic; Baltic (DOS)',
    850: 'OEM Multilingual Latin 1; Western European (DOS)',
    852: 'OEM Latin 2; Central European (DOS)',
    855: 'OEM Cyrillic (primarily Russian)',
    857: 'OEM Turkish; Turkish (DOS)',
    858: 'OEM Multilingual Latin 1 + Euro symbol',
    860: 'OEM Portuguese; Portuguese (DOS)',
    861: 'OEM Icelandic; Icelandic (DOS)',
    862: 'OEM Hebrew; Hebrew (DOS)',
    863: 'OEM French Canadian; French Canadian (DOS)',
    864: 'OEM Arabic; Arabic (864)',
    865: 'OEM Nordic; Nordic (DOS)',
    866: 'OEM Russian; Cyrillic (DOS)',
    869: 'OEM Modern Greek; Greek, Modern (DOS)',
    870: 'IBM EBCDIC Multilingual/ROECE (Latin 2); IBM EBCDIC Multilingual Latin 2',
    874: 'ANSI/OEM Thai (ISO 8859-11); Thai (Windows)',
    875: 'IBM EBCDIC Greek Modern',
    932: 'ANSI/OEM Japanese; Japanese (Shift-JIS)',
    936: 'ANSI/OEM Simplified Chinese (PRC, Singapore); Chinese Simplified (GB2312)',
    949: 'ANSI/OEM Korean (Unified Hangul Code)',
    950: 'ANSI/OEM Traditional Chinese (Taiwan; Hong Kong SAR, PRC); Chinese Traditional (Big5)',
    1026: 'IBM EBCDIC Turkish (Latin 5)',
    1047: 'IBM EBCDIC Latin 1/Open System',
    1140: 'IBM EBCDIC US-Canada (037 + Euro symbol); IBM EBCDIC (US-Canada-Euro)',
    1141: 'IBM EBCDIC Germany (20273 + Euro symbol); IBM EBCDIC (Germany-Euro)',
    1142: 'IBM EBCDIC Denmark-Norway (20277 + Euro symbol); IBM EBCDIC (Denmark-Norway-Euro)',
    1143: 'IBM EBCDIC Finland-Sweden (20278 + Euro symbol); IBM EBCDIC (Finland-Sweden-Euro)',
    1144: 'IBM EBCDIC Italy (20280 + Euro symbol); IBM EBCDIC (Italy-Euro)',
    1145: 'IBM EBCDIC Latin America-Spain (20284 + Euro symbol); IBM EBCDIC (Spain-Euro)',
    1146: 'IBM EBCDIC United Kingdom (20285 + Euro symbol); IBM EBCDIC (UK-Euro)',
    1147: 'IBM EBCDIC France (20297 + Euro symbol); IBM EBCDIC (France-Euro)',
    1148: 'IBM EBCDIC International (500 + Euro symbol); IBM EBCDIC (International-Euro)',
    1149: 'IBM EBCDIC Icelandic (20871 + Euro symbol); IBM EBCDIC (Icelandic-Euro)',
    1200: 'Unicode UTF-16, little endian byte order (BMP of ISO 10646); available only to managed applications',
    1201: 'Unicode UTF-16, big endian byte order; available only to managed applications',
    1250: 'ANSI Central European; Central European (Windows)',
    1251: 'ANSI Cyrillic; Cyrillic (Windows)',
    1252: 'ANSI Latin 1; Western European (Windows)',
    1253: 'ANSI Greek; Greek (Windows)',
    1254: 'ANSI Turkish; Turkish (Windows)',
    1255: 'ANSI Hebrew; Hebrew (Windows)',
    1256: 'ANSI Arabic; Arabic (Windows)',
    1257: 'ANSI Baltic; Baltic (Windows)',
    1258: 'ANSI/OEM Vietnamese; Vietnamese (Windows)',
    1361: 'Korean (Johab)',
    10000: 'MAC Roman; Western European (Mac)',
    10001: 'Japanese (Mac)',
    10002: 'MAC Traditional Chinese (Big5); Chinese Traditional (Mac)',
    10003: 'Korean (Mac)',
    10004: 'Arabic (Mac)',
    10005: 'Hebrew (Mac)',
    10006: 'Greek (Mac)',
    10007: 'Cyrillic (Mac)',
    10008: 'MAC Simplified Chinese (GB 2312); Chinese Simplified (Mac)',
    10010: 'Romanian (Mac)',
    10017: 'Ukrainian (Mac)',
    10021: 'Thai (Mac)',
    10029: 'MAC Latin 2; Central European (Mac)',
    10079: 'Icelandic (Mac)',
    10081: 'Turkish (Mac)',
    10082: 'Croatian (Mac)',
    12000: 'Unicode UTF-32, little endian byte order; available only to managed applications',
    12001: 'Unicode UTF-32, big endian byte order; available only to managed applications',
    20000: 'CNS Taiwan; Chinese Traditional (CNS)',
    20001: 'TCA Taiwan',
    20002: 'Eten Taiwan; Chinese Traditional (Eten)',
    20003: 'IBM5550 Taiwan',
    20004: 'TeleText Taiwan',
    20005: 'Wang Taiwan',
    20105: 'IA5 (IRV International Alphabet No. 5, 7-bit); Western European (IA5)',
    20106: 'IA5 German (7-bit)',
    20107: 'IA5 Swedish (7-bit)',
    20108: 'IA5 Norwegian (7-bit)',
    20127: 'US-ASCII (7-bit)',
    20261: 'T.61',
    20269: 'ISO 6937 Non-Spacing Accent',
    20273: 'IBM EBCDIC Germany',
    20277: 'IBM EBCDIC Denmark-Norway',
    20278: 'IBM EBCDIC Finland-Sweden',
    20280: 'IBM EBCDIC Italy',
    20284: 'IBM EBCDIC Latin America-Spain',
    20285: 'IBM EBCDIC United Kingdom',
    20290: 'IBM EBCDIC Japanese Katakana Extended',
    20297: 'IBM EBCDIC France',
    20420: 'IBM EBCDIC Arabic',
    20423: 'IBM EBCDIC Greek',
    20424: 'IBM EBCDIC Hebrew',
    20833: 'IBM EBCDIC Korean Extended',
    20838: 'IBM EBCDIC Thai',
    20866: 'Russian (KOI8-R); Cyrillic (KOI8-R)',
    20871: 'IBM EBCDIC Icelandic',
    20880: 'IBM EBCDIC Cyrillic Russian',
    20905: 'IBM EBCDIC Turkish',
    20924: 'IBM EBCDIC Latin 1/Open System (1047 + Euro symbol)',
    20932: 'Japanese (JIS 0208-1990 and 0212-1990)',
    20936: 'Simplified Chinese (GB2312); Chinese Simplified (GB2312-80)',
    20949: 'Korean Wansung',
    21025: 'IBM EBCDIC Cyrillic Serbian-Bulgarian',
    21027: '(deprecated)',
    21866: 'Ukrainian (KOI8-U); Cyrillic (KOI8-U)',
    28591: 'ISO 8859-1 Latin 1; Western European (ISO)',
    28592: 'ISO 8859-2 Central European; Central European (ISO)',
    28593: 'ISO 8859-3 Latin 3',
    28594: 'ISO 8859-4 Baltic',
    28595: 'ISO 8859-5 Cyrillic',
    28596: 'ISO 8859-6 Arabic',
    28597: 'ISO 8859-7 Greek',
    28598: 'ISO 8859-8 Hebrew; Hebrew (ISO-Visual)',
    28599: 'ISO 8859-9 Turkish',
    28603: 'ISO 8859-13 Estonian',
    28605: 'ISO 8859-15 Latin 9',
    29001: 'Europa 3',
    38598: 'ISO 8859-8 Hebrew; Hebrew (ISO-Logical)',
    50220: 'ISO 2022 Japanese with no halfwidth Katakana; Japanese (JIS)',
    50221: 'ISO 2022 Japanese with halfwidth Katakana; Japanese (JIS-Allow 1 byte Kana)',
    50222: 'ISO 2022 Japanese JIS X 0201-1989; Japanese (JIS-Allow 1 byte Kana - SO/SI)',
    50225: 'ISO 2022 Korean',
    50227: 'ISO 2022 Simplified Chinese; Chinese Simplified (ISO 2022)',
    50229: 'ISO 2022 Traditional Chinese',
    50930: 'EBCDIC Japanese (Katakana) Extended',
    50931: 'EBCDIC US-Canada and Japanese',
    50933: 'EBCDIC Korean Extended and Korean',
    50935: 'EBCDIC Simplified Chinese Extended and Simplified Chinese',
    50936: 'EBCDIC Simplified Chinese',
    50937: 'EBCDIC US-Canada and Traditional Chinese',
    50939: 'EBCDIC Japanese (Latin) Extended and Japanese',
    51932: 'EUC Japanese',
    51936: 'EUC Simplified Chinese; Chinese Simplified (EUC)',
    51949: 'EUC Korean',
    51950: 'EUC Traditional Chinese',
    52936: 'HZ-GB2312 Simplified Chinese; Chinese Simplified (HZ)',
    54936: 'Windows XP and later: GB18030 Simplified Chinese (4 byte); Chinese Simplified (GB18030)',
    57002: 'ISCII Devanagari',
    57003: 'ISCII Bengali',
    57004: 'ISCII Tamil',
    57005: 'ISCII Telugu',
    57006: 'ISCII Assamese',
    57007: 'ISCII Oriya',
    57008: 'ISCII Kannada',
    57009: 'ISCII Malayalam',
    57010: 'ISCII Gujarati',
    57011: 'ISCII Punjabi',
    65000: 'Unicode (UTF-7)',
    65001: 'Unicode (UTF-8)'
}

def LookupCodepage(codepage):
    if codepage in dCodepages:
        return dCodepages[codepage]
    else:
        return ''

def MyRepr(stringArg):
    stringRepr = repr(stringArg)
    if "'" + stringArg + "'" != stringRepr:
        return stringRepr
    else:
        return stringArg

def FindAll(data, sub):
    result = []
    start = 0
    while True:
        position = data.find(sub, start)
        if position == -1:
            return result
        result.append(position)
        start = position + 1

def HeuristicDecompress(data):
    for position in FindAll(data, '\x78'):
        try:
            return zlib.decompress(data[position:])
        except:
            pass
    return data

CUTTERM_NOTHING = 0
CUTTERM_POSITION = 1
CUTTERM_FIND = 2
CUTTERM_LENGTH = 3

def Replace(string, dReplacements):
    if string in dReplacements:
        return dReplacements[string]
    else:
        return string

def ParseCutTerm(argument):
    if argument == '':
        return CUTTERM_NOTHING, None, ''
    oMatch = re.match(r'\-?0x([0-9a-f]+)', argument, re.I)
    if oMatch == None:
        oMatch = re.match(r'\-?(\d+)', argument)
    else:
        value = int(oMatch.group(1), 16)
        if argument.startswith('-'):
            value = -value
        return CUTTERM_POSITION, value, argument[len(oMatch.group(0)):]
    if oMatch == None:
        oMatch = re.match(r'\[([0-9a-f]+)\](\d+)?([+-]\d+)?', argument, re.I)
    else:
        value = int(oMatch.group(1))
        if argument.startswith('-'):
            value = -value
        return CUTTERM_POSITION, value, argument[len(oMatch.group(0)):]
    if oMatch == None:
        oMatch = re.match(r"\[\'(.+?)\'\](\d+)?([+-]\d+)?", argument)
    else:
        if len(oMatch.group(1)) % 2 == 1:
            raise Exception("Uneven length hexadecimal string")
        else:
            return CUTTERM_FIND, (binascii.a2b_hex(oMatch.group(1)), int(Replace(oMatch.group(2), {None: '1'})), int(Replace(oMatch.group(3), {None: '0'}))), argument[len(oMatch.group(0)):]
    if oMatch == None:
        return None, None, argument
    else:
        return CUTTERM_FIND, (oMatch.group(1), int(Replace(oMatch.group(2), {None: '1'})), int(Replace(oMatch.group(3), {None: '0'}))), argument[len(oMatch.group(0)):]

def ParseCutArgument(argument):
    type, value, remainder = ParseCutTerm(argument.strip())
    if type == CUTTERM_NOTHING:
        return CUTTERM_NOTHING, None, CUTTERM_NOTHING, None
    elif type == None:
        if remainder.startswith(':'):
            typeLeft = CUTTERM_NOTHING
            valueLeft = None
            remainder = remainder[1:]
        else:
            return None, None, None, None
    else:
        typeLeft = type
        valueLeft = value
        if typeLeft == CUTTERM_POSITION and valueLeft < 0:
            return None, None, None, None
        if typeLeft == CUTTERM_FIND and valueLeft[1] == 0:
            return None, None, None, None
        if remainder.startswith(':'):
            remainder = remainder[1:]
        else:
            return None, None, None, None
    type, value, remainder = ParseCutTerm(remainder)
    if type == CUTTERM_POSITION and remainder == 'l':
        return typeLeft, valueLeft, CUTTERM_LENGTH, value
    elif type == None or remainder != '':
        return None, None, None, None
    elif type == CUTTERM_FIND and value[1] == 0:
        return None, None, None, None
    else:
        return typeLeft, valueLeft, type, value

def Find(data, value, nth):
    position = -1
    while nth > 0:
        position = data.find(value, position + 1)
        if position == -1:
            return -1
        nth -= 1
    return position

def CutData(stream, cutArgument):
    if cutArgument == '':
        return stream

    typeLeft, valueLeft, typeRight, valueRight = ParseCutArgument(cutArgument)

    if typeLeft == None:
        return stream

    if typeLeft == CUTTERM_NOTHING:
        positionBegin = 0
    elif typeLeft == CUTTERM_POSITION:
        positionBegin = valueLeft
    elif typeLeft == CUTTERM_FIND:
        positionBegin = Find(stream, valueLeft[0], valueLeft[1])
        if positionBegin == -1:
            return ''
        positionBegin += valueLeft[2]
    else:
        raise Exception("Unknown value typeLeft")

    if typeRight == CUTTERM_NOTHING:
        positionEnd = len(stream)
    elif typeRight == CUTTERM_POSITION and valueRight < 0:
        positionEnd = len(stream) + valueRight
    elif typeRight == CUTTERM_POSITION:
        positionEnd = valueRight + 1
    elif typeRight == CUTTERM_LENGTH:
        positionEnd = positionBegin + valueRight
    elif typeRight == CUTTERM_FIND:
        positionEnd = Find(stream, valueRight[0], valueRight[1])
        if positionEnd == -1:
            return ''
        else:
            positionEnd += len(valueRight[0])
        positionEnd += valueRight[2]
    else:
        raise Exception("Unknown value typeRight")

    return stream[positionBegin:positionEnd]

def ExtraInfoMD5(data):
    return hashlib.md5(data).hexdigest()

def ExtraInfoSHA1(data):
    return hashlib.sha1(data).hexdigest()

def ExtraInfoSHA256(data):
    return hashlib.sha256(data).hexdigest()

def CalculateByteStatistics(dPrevalence):
    sumValues = sum(dPrevalence.values())
    countNullByte = dPrevalence[0]
    countControlBytes = 0
    countWhitespaceBytes = 0
    for iter in range(1, 0x21):
        if chr(iter) in string.whitespace:
            countWhitespaceBytes += dPrevalence[iter]
        else:
            countControlBytes += dPrevalence[iter]
    countControlBytes += dPrevalence[0x7F]
    countPrintableBytes = 0
    for iter in range(0x21, 0x7F):
        countPrintableBytes += dPrevalence[iter]
    countHighBytes = 0
    for iter in range(0x80, 0x100):
        countHighBytes += dPrevalence[iter]
    entropy = 0.0
    for iter in range(0x100):
        if dPrevalence[iter] > 0:
            prevalence = float(dPrevalence[iter]) / float(sumValues)
            entropy += - prevalence * math.log(prevalence, 2)
    return sumValues, entropy, countNullByte, countControlBytes, countWhitespaceBytes, countPrintableBytes, countHighBytes

def ExtraInfoENTROPY(data):
    dPrevalence = {iter: 0 for iter in range(0x100)}
    for char in data:
        dPrevalence[ord(char)] += 1
    sumValues, entropy, countNullByte, countControlBytes, countWhitespaceBytes, countPrintableBytes, countHighBytes = CalculateByteStatistics(dPrevalence)
    return '%f' % entropy

def ExtraInfoHEADHEX(data):
    return binascii.hexlify(data[:16])

def ExtraInfoHEADASCII(data):
    return ''.join([IFF(ord(b) >= 32, b, '.') for b in data[:16]])

def ExtraInfoTAILHEX(data):
    return binascii.hexlify(data[-16:])

def ExtraInfoTAILASCII(data):
    return ''.join([IFF(ord(b) >= 32, b, '.') for b in data[-16:]])

def ExtraInfoHISTOGRAM(data):
    dPrevalence = {iter: 0 for iter in range(0x100)}
    for char in data:
        dPrevalence[ord(char)] += 1
    result = []
    count = 0
    minimum = None
    maximum = None
    for iter in range(0x100):
        if dPrevalence[iter] > 0:
            result.append('0x%02x:%d' % (iter, dPrevalence[iter]))
            count += 1
            if minimum == None:
                minimum = iter
            else:
                minimum = min(minimum, iter)
            if maximum == None:
                maximum = iter
            else:
                maximum = max(maximum, iter)
    result.insert(0, '%d' % count)
    result.insert(1, IFF(minimum == None, '', '0x%02x' % minimum))
    result.insert(2, IFF(maximum == None, '', '0x%02x' % maximum))
    return ','.join(result)

def ExtraInfoBYTESTATS(data):
    dPrevalence = {iter: 0 for iter in range(0x100)}
    for char in data:
        dPrevalence[ord(char)] += 1
    sumValues, entropy, countNullByte, countControlBytes, countWhitespaceBytes, countPrintableBytes, countHighBytes = CalculateByteStatistics(dPrevalence)
    return '%d,%d,%d,%d,%d' % (countNullByte, countControlBytes, countWhitespaceBytes, countPrintableBytes, countHighBytes)

def GenerateExtraInfo(extra, index, indicator, name, stream):
    if extra == '':
        return ''
    if extra.startswith('!'):
        extra = extra[1:]
        prefix = ''
    else:
        prefix = ' '
    if indicator == ' ':
        indicator = ''
    dExtras = {'%INDEX%': lambda x: index,
               '%INDICATOR%': lambda x: indicator,
               '%LENGTH%': lambda x: '%d' % len(stream),
               '%NAME%': lambda x: name,
               '%MD5%': ExtraInfoMD5,
               '%SHA1%': ExtraInfoSHA1,
               '%SHA256%': ExtraInfoSHA256,
               '%ENTROPY%': ExtraInfoENTROPY,
               '%HEADHEX%': ExtraInfoHEADHEX,
               '%HEADASCII%': ExtraInfoHEADASCII,
               '%TAILHEX%': ExtraInfoTAILHEX,
               '%TAILASCII%': ExtraInfoTAILASCII,
               '%HISTOGRAM%': ExtraInfoHISTOGRAM,
               '%BYTESTATS%': ExtraInfoBYTESTATS,
              }
    for variable in dExtras:
        if variable in extra:
            extra = extra.replace(variable, dExtras[variable](stream))
    return prefix + extra.replace(r'\t', '\t').replace(r'\n', '\n')

def OLE10HeaderPresent(data):
    length = len(data)
    if length < 6:
        return False
    size, data = ReadDWORD(data)
    if size == None:
        return False
    if size + 4 != length:
        return False
    version, data = ReadWORD(data)
    return version ==2

def OLEGetStreams(ole):
    olestreams = []
    for fname in ole.listdir():
        olestreams.append([0, fname, ole.get_type(fname), ole.openstream(fname).read()])
    for sid in range(len(ole.direntries)):
        entry = ole.direntries[sid]
        if entry is None:
            entry = ole._load_direntry(sid)
            if entry.entry_type == 2:
                olestreams.append([1, entry.name, entry.entry_type, ole._open(entry.isectStart, entry.size).read()])
    return olestreams

def OLESub(ole, prefix, rules, options):
    global plugins
    global decoders

    returnCode = 1

    if options.metadata:
        metadata = ole.get_metadata()
        print('Properties SummaryInformation:')
        for attribute in metadata.SUMMARY_ATTRIBS:
            value = getattr(metadata, attribute)
            if value != None:
                if attribute == 'codepage':
                    print(' %s: %s %s' % (attribute, value, LookupCodepage(value)))
                else:
                    print(' %s: %s' % (attribute, value))
        print('Properties DocumentSummaryInformation:')
        for attribute in metadata.DOCSUM_ATTRIBS:
            value = getattr(metadata, attribute)
            if value != None:
                if attribute == 'codepage_doc':
                    print(' %s: %s %s' % (attribute, value, LookupCodepage(value)))
                else:
                    print(' %s: %s' % (attribute, value))
        return returnCode

    if options.jsonoutput:
        object = []
        counter = 1
        for orphan, fname, entry_type, stream in OLEGetStreams(ole):
            object.append({'id': counter, 'name': PrintableName(fname), 'content': binascii.b2a_base64(stream).strip('\n')})
            counter += 1
        print(json.dumps({'version': 1, 'fields': ['id', 'name', 'content'], 'items': object}))
        return

    if options.select == '':
        counter = 1
        vbaConcatenate = ''
        for orphan, fname, entry_type, stream in OLEGetStreams(ole):
            indicator = ' '
            macroPresent = False
            lengthString = '      '
            if entry_type == 1:
                indicator = '.'
            elif entry_type == 2:
                lengthString = '%7d' % len(stream)
                macroPresent = FindCompression(stream) != -1
# MADE CHANGES HERE START ######################################################################################
#Most of the core data parsing and sorting happens here
#this peace of code find all the ole's and macros streams in the document
                if macroPresent:
                    returnCode = 2
                    if not SearchAndDecompressSub(stream)[0]:
                        indicator = 'E'
                    else:
                        indicator = 'M'
                        if MacrosContainsOnlyAttributesOrOptions(stream):
                            indicator = 'm'
                elif OLE10HeaderPresent(stream):
                    indicator = 'O'
            index = '%s%d' % (prefix, counter)
            if not options.quiet:
            #magic happens
                line = '%s: %s %s %s' % (index, indicator, lengthString, PrintableName(fname, orphan))

                if indicator.lower() == 'm' and options.vbadecompress:
                    streamForExtra = SearchAndDecompress(stream)
                else:
                    streamForExtra = stream
                if options.calc:
                    line += ' %s' % hashlib.md5(streamForExtra).hexdigest()
                if options.extra.startswith('!'):
                    line = ''
                line += GenerateExtraInfo(options.extra, index, indicator, PrintableName(fname, orphan), streamForExtra)
            #indicator tells us weather its a macro on ole
            #if value of indicator is O or o its an ole
            if indicator == 'O' or indicator == 'o':
                #print(index)

                # executing a shell command to decode that particular macro
                #using nearly original oledump.py librar main file
                olex.ProcessOLE([getDirName()],index)
                #dump = files = subprocess.Popen(que, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                global st_ring
                global pic
                #for d in dump.stdout.readlines():
                #    pic = pic + d
                pic = pic+olex.return_data+";\n"
                #st_ring was frist being used to directly send data to client
                #now data prcessing is being done on service side
                #changing whole code was time consuming therefore im using pic to store st_ring data for processing
                #processed data will be saved into st_ring
                #To Do : Create function for json string processing

# CHANGES END HERE ######################################################################################
            for cPlugin in plugins:
                try:
                    if cPlugin.macroOnly and macroPresent:
                        oPlugin = cPlugin(fname, SearchAndDecompress(stream), options.pluginoptions)
                    elif not cPlugin.macroOnly:
                        oPlugin = cPlugin(fname, stream, options.pluginoptions)
                    else:
                        oPlugin = None
                except Exception as e:
                    print('Error instantiating plugin: %s' % cPlugin.name)
                    if options.verbose:
                        raise e
                    return returnCode
                if oPlugin != None:
                    result = oPlugin.Analyze()
                    if oPlugin.ran:
                        if options.quiet:
                            if oPlugin.indexQuiet:
                                if result != []:
                                    print('%3s: %s' % (index, MyRepr(result[0])))
                            else:
                                for line in result:
                                    print(MyRepr(line))
                        else:
                            print('               Plugin: %s ' % oPlugin.name)
                            for line in result:
                                print('                 ' + MyRepr(line))
            counter += 1
            if options.yara != None:
                oDecoders = [cIdentity(stream, None)]
                for cDecoder in decoders:
                    try:
                        oDecoder = cDecoder(stream, options.decoderoptions)
                        oDecoders.append(oDecoder)
                    except Exception as e:
                        print('Error instantiating decoder: %s' % cDecoder.name)
                        if options.verbose:
                            raise e
                        return returnCode
                for oDecoder in oDecoders:
                    while oDecoder.Available():
                        for result in rules.match(data=oDecoder.Decode(), externals={'streamname': PrintableName(fname), 'VBA': False}):
                            print('               YARA rule%s: %s' % (IFF(oDecoder.Name() == '', '', ' (stream decoder: %s)' % oDecoder.Name()), result.rule))
                            if options.yarastrings:
                                for stringdata in result.strings:
                                    print('               %06x %s:' % (stringdata[0], stringdata[1]))
                                    print('                %s' % binascii.hexlify(C2BIP3(stringdata[2])))
                                    print('                %s' % repr(stringdata[2]))
            if indicator.lower() == 'm':
                vbaConcatenate += SearchAndDecompress(stream) + '\n'
        if options.yara != None and vbaConcatenate != '':
            print('All VBA source code:')
            for result in rules.match(data=vbaConcatenate, externals={'streamname': '', 'VBA': True}):
                print('               YARA rule: %s' % result.rule)
                if options.yarastrings:
                    for stringdata in result.strings:
                        print('               %06x %s:' % (stringdata[0], stringdata[1]))
                        print('                %s' % binascii.hexlify(C2BIP3(stringdata[2])))
                        print('                %s' % repr(stringdata[2]))
    else:
        if len(decoders) > 1:
            print('Error: provide only one decoder when using option select')
            return returnCode
        if options.decompress:
            DecompressFunction = HeuristicDecompress
        else:
            DecompressFunction = lambda x:x
        if options.dump:
            DumpFunction = lambda x:x
            IfWIN32SetBinary(sys.stdout)
        elif options.hexdump:
            DumpFunction = HexDump
        elif options.vbadecompress:
            if options.select == 'a':
                DumpFunction = lambda x: SearchAndDecompress(x, '')
            else:
                DumpFunction = SearchAndDecompress
        elif options.vbadecompresscorrupt:
            DumpFunction = lambda x: SearchAndDecompress(x, None)
        elif options.extract:
            DumpFunction = Extract
            IfWIN32SetBinary(sys.stdout)
        elif options.info:
            DumpFunction = Info
        elif options.translate != '':
            DumpFunction = Translate(options.translate)
        elif options.strings:
            DumpFunction = DumpFunctionStrings
        else:
            DumpFunction = HexAsciiDump
        counter = 1
        for orphan, fname, entry_type, stream in OLEGetStreams(ole):
            if options.select == 'a' or ('%s%d' % (prefix, counter)) == options.select or prefix == 'A' and str(counter) == options.select:
                StdoutWriteChunked(DumpFunction(DecompressFunction(DecodeFunction(decoders, options, CutData(stream, options.cut)))))
                if options.select != 'a':
                    break
            counter += 1

    return returnCode

def YARACompile(ruledata):
    if ruledata.startswith('#'):
        if ruledata.startswith('#h#'):
            rule = binascii.a2b_hex(ruledata[3:])
        elif ruledata.startswith('#b#'):
            rule = binascii.a2b_base64(ruledata[3:])
        elif ruledata.startswith('#s#'):
            rule = 'rule string {strings: $a = "%s" ascii wide nocase condition: $a}' % ruledata[3:]
        elif ruledata.startswith('#q#'):
            rule = ruledata[3:].replace("'", '"')
        else:
            rule = ruledata[1:]
        return yara.compile(source=rule, externals={'streamname': '', 'VBA': False})
    else:
        dFilepaths = {}
        if os.path.isdir(ruledata):
            for root, dirs, files in os.walk(ruledata):
                for file in files:
                    filename = os.path.join(root, file)
                    dFilepaths[filename] = filename
        else:
            for filename in ProcessAt(ruledata):
                dFilepaths[filename] = filename
        return yara.compile(filepaths=dFilepaths, externals={'streamname': '', 'VBA': False})

def FilenameInSimulations(filename):
    if dslsimulationdb == None:
        return False
    return filename in dslsimulationdb.dSimulations

def OLEDump(filename, options):
    returnCode = 0

    if filename != '' and not FilenameInSimulations(filename) and not os.path.isfile(filename):
        print('Error: %s is not a file.' % filename)
        return returnCode

    global plugins
    plugins = []
    LoadPlugins(options.plugins, options.plugindir, True)

    global decoders
    decoders = []
    LoadDecoders(options.decoders, options.decoderdir, True)

    if options.raw:
        if filename == '':
            IfWIN32SetBinary(sys.stdin)
            data = sys.stdin.read()
        else:
            data = File2String(filename)
        if options.vbadecompress:
            if options.vbadecompresscorrupt:
                vba = SearchAndDecompress(data, None)
            else:
                vba = SearchAndDecompress(data)
            if options.plugins == '':
                print(vba)
                return returnCode
            else:
                data = vba
        for cPlugin in plugins:
            try:
                if cPlugin.macroOnly:
                    oPlugin = cPlugin(filename, data, options.pluginoptions)
                elif not cPlugin.macroOnly:
                    oPlugin = cPlugin(filename, data, options.pluginoptions)
                else:
                    oPlugin = None
            except Exception as e:
                print('Error instantiating plugin: %s' % cPlugin.name)
                if options.verbose:
                    raise e
                return returnCode
            if oPlugin != None:
                result = oPlugin.Analyze()
                if oPlugin.ran:
                    if options.quiet:
                        for line in result:
                            print(MyRepr(line))
                    else:
                        print('Plugin: %s ' % oPlugin.name)
                        for line in result:
                            print(' ' + MyRepr(line))
        return returnCode

    rules = None
    if options.yara != None:
        if not 'yara' in sys.modules:
            print('Error: option yara requires the YARA Python module.')
            return returnCode
        rules = YARACompile(options.yara)

    if filename == '':
        IfWIN32SetBinary(sys.stdin)
        oStringIO = cStringIO.StringIO(sys.stdin.read())
    elif FilenameInSimulations(filename):
        oZipfile = zipfile.ZipFile(dslsimulationdb.GetSimulation(filename), 'r')
        oZipContent = oZipfile.open(oZipfile.infolist()[0], 'r', C2BIP3(MALWARE_PASSWORD))
        zipContent = oZipContent.read()
        if zipContent.startswith('Neut'):
            zipContent = OLEFILE_MAGIC + zipContent[4:]
        oStringIO = cStringIO.StringIO(zipContent)
        oZipContent.close()
        oZipfile.close()
    elif filename.lower().endswith('.zip'):
        oZipfile = zipfile.ZipFile(filename, 'r')
        oZipContent = oZipfile.open(oZipfile.infolist()[0], 'r', C2BIP3(MALWARE_PASSWORD))
        oStringIO = cStringIO.StringIO(oZipContent.read())
        oZipContent.close()
        oZipfile.close()
    else:
        oStringIO = cStringIO.StringIO(open(filename, 'rb').read())

    magic = oStringIO.read(6)
    oStringIO.seek(0)
    if magic[0:4] == OLEFILE_MAGIC:
        ole = olefile.OleFileIO(oStringIO)
        returnCode = OLESub(ole, '', rules, options)
        ole.close()
    elif magic[0:2] == 'PK':
        oZipfile = zipfile.ZipFile(oStringIO, 'r')
        counter = 0
        for info in oZipfile.infolist():
            oZipContent = oZipfile.open(info, 'r')
            content = oZipContent.read()
            if content[0:4] == OLEFILE_MAGIC:
                letter = chr(ord('A') + counter)
                counter += 1
                if options.select == '':
                    if not options.quiet and not options.jsonoutput:
                        print('%s: %s' % (letter, info.filename))
                ole = olefile.OleFileIO(cStringIO.StringIO(content))
                returnCode = OLESub(ole, letter, rules, options)
                ole.close()
            oZipContent.close()
        oZipfile.close()
    else:
        data = oStringIO.read()
        oStringIO.seek(0)
        if '<?xml' in data:
            try:
                oXML = xml.dom.minidom.parse(oStringIO)
            except:
                print('Error: parsing %s as XML.' % filename)
                return -1
            counter = 0
            for oElement in oXML.getElementsByTagName('*'):
                if oElement.firstChild and oElement.firstChild.nodeValue:
                    try:
                        data = binascii.a2b_base64(oElement.firstChild.nodeValue)
                    except binascii.Error:
                        data = ''
                    except UnicodeEncodeError:
                        data = ''
                    content = data
                    if content.startswith(ACTIVEMIME_MAGIC):
                        content = HeuristicDecompress(content)
                    if content[0:4] == OLEFILE_MAGIC:
                        letter = chr(ord('A') + counter)
                        counter += 1
                        if options.select == '':
                            if not options.quiet:
                                nameValue = ''
                                for key, value in oElement.attributes.items():
                                    if key.endswith(':name'):
                                        nameValue = value
                                        break
                                print('%s: %s' % (letter, nameValue))
                        ole = olefile.OleFileIO(cStringIO.StringIO(content))
                        returnCode = OLESub(ole, letter, rules, options)
                        ole.close()
        elif data.startswith(ACTIVEMIME_MAGIC):
            content = HeuristicDecompress(data)
            if content[0:4] == OLEFILE_MAGIC:
                ole = olefile.OleFileIO(cStringIO.StringIO(content))
                returnCode = OLESub(ole, '', rules, options)
                ole.close()
        else:
            print('Error: %s is not a valid OLE file.' % filename)

    return returnCode
def ProcessString(st_ring):
    st_ring = "{"
    result = pic.split("\n")
    # parsing output from shell command execution to get required data
    for line in result:
        if line.startswith("String 1:"):
            # ole name e.g "zmq.c"
            i = line.index(":")
            name = line[i + 2:len(line)]
            # getting extension type
            i = name.index(".")
            ext = name[i + 1:len(name)]
            st_ring = st_ring + '"name":"{0}","ext":"{1}",'.format(name, ext)
        if line.startswith("Size embedded file:"):
            i = line.index(":")
            size = line[i + 2:len(line)]
            st_ring = st_ring + '"size":"{0}",'.format(size)
        if line.startswith("MAGIC:"):
            i = line.index(":")
            magic = line[i + 12:len(line)]
            st_ring = st_ring + '"magic":"{0}"'.format(magic)
        if line.startswith(";"):
            st_ring = st_ring + "};{"
    st_ring = st_ring[:-2]
    return st_ring
def OptionsEnvironmentVariables(options):
    if options.extra == '':
        options.extra = os.getenv('OLEDUMP_EXTRA', options.extra)
def GetInformation(f_location):
    oParser = optparse.OptionParser(usage='usage: %prog [options] [file]\n' + __description__, version='%prog ' + __version__)
    oParser.add_option('-m', '--man', action='store_true', default=False, help='Print manual')
    oParser.add_option('-s', '--select', default='', help='select item nr for dumping (a for all)')
    oParser.add_option('-d', '--dump', action='store_true', default=False, help='perform dump')
    oParser.add_option('-x', '--hexdump', action='store_true', default=False, help='perform hex dump')
    oParser.add_option('-a', '--asciidump', action='store_true', default=False, help='perform ascii dump')
    oParser.add_option('-S', '--strings', action='store_true', default=False, help='perform strings dump')
    oParser.add_option('-v', '--vbadecompress', action='store_true', default=False, help='VBA decompression')
    oParser.add_option('--vbadecompresscorrupt', action='store_true', default=False, help='VBA decompression, display beginning if corrupted')
    oParser.add_option('-r', '--raw', action='store_true', default=False, help='read raw file (use with options -v or -p')
    oParser.add_option('-t', '--translate', type=str, default='', help='string translation, like utf16 or .decode("utf8")')
    oParser.add_option('-e', '--extract', action='store_true', default=False, help='extract OLE embedded file')
    oParser.add_option('-i', '--info', action='store_true', default=False, help='print extra info for selected item')
    oParser.add_option('-p', '--plugins', type=str, default='', help='plugins to load (separate plugins with a comma , ; @file supported)')
    oParser.add_option('--pluginoptions', type=str, default='', help='options for the plugin')
    oParser.add_option('--plugindir', type=str, default='', help='directory for the plugin')
    oParser.add_option('-q', '--quiet', action='store_true', default=False, help='only print output from plugins')
    oParser.add_option('-y', '--yara', help="YARA rule-file, @file, directory or #rule to check streams (YARA search doesn't work with -s option)")
    oParser.add_option('-D', '--decoders', type=str, default='', help='decoders to load (separate decoders with a comma , ; @file supported)')
    oParser.add_option('--decoderoptions', type=str, default='', help='options for the decoder')
    oParser.add_option('--decoderdir', type=str, default='', help='directory for the decoder')
    oParser.add_option('--yarastrings', action='store_true', default=False, help='Print YARA strings')
    oParser.add_option('-M', '--metadata', action='store_true', default=False, help='Print metadata')
    oParser.add_option('-c', '--calc', action='store_true', default=False, help='Add extra calculated data to output, like hashes')
    oParser.add_option('--decompress', action='store_true', default=False, help='Search for compressed data in the stream and decompress it')
    oParser.add_option('-V', '--verbose', action='store_true', default=False, help='verbose output with decoder errors')
    oParser.add_option('-C', '--cut', type=str, default='', help='cut data')
    oParser.add_option('-E', '--extra', type=str, default='', help='add extra info (environment variable: OLEDUMP_EXTRA)')
    oParser.add_option('-j', '--jsonoutput', action='store_true', default=False, help='produce json output')
    oParser.add_option("-X", "--dir", type="string",help="List of directory",dest="inDir", default=".")
    (options, args) = oParser.parse_args()
#MADE CHANGES HERE START 01 ######################################################################################
#These Changes inlude implementation of zmq
#changing inferfacing mehtod
#error reporting
    global pic
    pic = ""
    setStringNull()

    #initializing zmq services
    #it has to be noted that zmq service is only initialized once
    args = [" "]
    args[0] = f_location

    setDirName(args[0])

    if ParseCutArgument(options.cut)[0] == None:
        print('Error: the expression of the cut option (-C) is invalid: %s' % options.cut)
        #return 0

    OptionsEnvironmentVariables(options)

    if len(args) > 1:
        oParser.print_help()
        #return 0
    #passing argument containing file location for processing
    OLEDump(args[0], options)

    processed_st_ring = ProcessString(pic)
    #st_ring is a global varibale which is being used as to get required result from
    #OLESub function in another class.
    #Data can't be directly accessed from OLESub function without making major changes to program
    #emptying global varible for use by next file to be processed
    return processed_st_ring
if __name__ == '__main__':
    sys.exit(GetInformation())
