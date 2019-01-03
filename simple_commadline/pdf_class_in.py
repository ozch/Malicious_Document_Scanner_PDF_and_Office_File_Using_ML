# -*- coding: utf-8 -*-
class pdfClass:
    def pdfScan(self, currentFile):
        self.filename1 = currentFile
        Featurelist = ['/0','/01','/07','/2','/3','/4','/5','/6','/7','/8','/9','/A','/AA','/AIS','/AN','/AP','/AS','/ASCII85Decode','/ASCIIHexDecode','/AcroForm','/Action','/Alternate','/Annots','/Arial','/ArtBox','/Author','/AvgWidth','/B','/BC','/BE','/BM','/BS','/BaseEncoding','/BaseFont','/BleedBox','/Border','/Btn','/C','/C0','/C2','/CA','/CCITTFaxDecode','/CIDFontType2','/CIDToGIDMap','/CS0','/CS1','/Catalog','/CharSet','/ColorSpace','/Colors','/Colors > 2^24','/Columns','/Count','/Courier','/CreationDate','/Creator','/CropBox','/DA','/DCTDecode','/DW','/Decode','/DecodeParms','/Default','/Dest','/DeviceGray','/DeviceRGB','/Differences','/E','/EF','/EmbeddedFile','/Encoding','/Euro','/ExtGState','/F1','/F10','/F11','/F2','/F3','/F4','/F5','/F6','/F7','/F8','/F9','/FS','/FT','/Ff','/Filespec','/Fit','/FitH','/Font','/FontBBox','/FontFile2','/FontMatrix','/FontStretch','/FontWeight','/Form','/FormType','/FunctionType','/G','/GS0','/GS1','/GS2','/Gamma','/GoTo','/Group','/H','/Helv','/Helvetica','/I','/ICCBased','/ID','/IF','/Identity','/Im0','/Im1','/Im2','/Im6','/Im7','/Im9','/ImageB','/ImageC','/ImageI','/ImageMask','/Indexed','/Info','/J','/JavaScript','/K','/Keywords','/Kids','/L','/L2R','/LZWDecode','/Lang','/Last','/Launch','/Leading','/Length1','/Linearized','/M','/MK','/MacRomanEncoding','/Marked','/Matrix','/MaxWidth','/MediaBox','/MissingWidth','/ModDate','/N','/Name','/Names','/Next','/None','/Normal','/O','/OCGs','/ON','/OP','/OPM','/ObjStm','/OneColumn','/OpenAction','/Outlines','/P','/PageLabels','/PageLayout','/PageMode','/Pages','/Parent','/PieceInfo','/Predictor','/Prev','/ProcSet','/Producer','/Properties','/Q','/R10','/R7','/R8','/R9','/Rect','/Resources','/Root','/Rotate','/S','/SA','/SM','/SMask','/Size','/StemH','/StemV','/StructParents','/StructTreeRoot','/Subj','/Subject','/Subtype','/Supplement','/T','/T1','/TP','/TT0','/TT1','/TT2','/TT4','/TU','/Tabs','/Text','/Threads','/Times','/TimesNewRomanPSMT','/Title','/ToUnicode','/Transparency','/Trapped','/TrimBox','/TrueType','/Type','/Type0','/Type1','/Type1C','/U','/URI','/UseOutlines','/V','/Version','/ViewerPreferences','/W','/Widget','/Width','/Widths','/WinAnsiEncoding','/X','/XHeight','/XObject','/XRef','/XRefStm','/XYZ','/Y','/Z','/a','/acute','/alpha','/arrowright','/asteriskmath','/at','/b','/beta','/bullet','/ca','/d','/dieresis','/e','/element','/endash','/f','/ff','/ffi','/fi','/fl','/g','/h','/i','/iX','/j','/k','/l','/less','/lessequal','/lslash','/minus','/mu','/multiply','/n','/o','/op','/p','/pdf','/pdftk','/pdfx','/percent','/periodcentered','/photoshop','/pi','/plus','/prime','/q','/question','/quotedblright','/quoteright','/r','/ring','/schema','/semicolon','/sigma','/slash','/space','/t','/thorn','/u','/v','/w','/www','/x','/xap','/xapMM','/xfa','/xmpMM','/y','/ydieresis','/z','/zcaron','/zero','/ÃŸ','After last EOF','obj','startxref','stream','xref','/255','/63','/Comment','/CourierStd','/DR','/Dests','/Direction','/Encrypt','/Fields','/Nums','/OCProperties','/PV','/PageDirection','/RichMedia','/SinglePage','/UseNone','/XFA','/Xilter','/XlateDecode','/field','/pageArea','/pageSet','/script','/subform','/template','/ui']
        tobeNumerical = ['/0','/01','/07','/2','/3','/4','/5','/6','/7','/8','/9','/A','/AA','/AIS','/AN','/AP','/AS','/ASCII85Decode','/ASCIIHexDecode','/AcroForm','/Action','/Alternate','/Annots','/Arial','/ArtBox','/Author','/AvgWidth','/B','/BC','/BE','/BM','/BS','/BaseEncoding','/BaseFont','/BleedBox','/Border','/Btn','/C','/C0','/C2','/CA','/CCITTFaxDecode','/CIDFontType2','/CIDToGIDMap','/CS0','/CS1','/Catalog','/CharSet','/ColorSpace','/Colors','/Colors > 2^24','/Columns','/Count','/Courier','/CreationDate','/Creator','/CropBox','/DA','/DCTDecode','/DW','/Decode','/DecodeParms','/Default','/Dest','/DeviceGray','/DeviceRGB','/Differences','/E','/EF','/EmbeddedFile','/Encoding','/Euro','/ExtGState','/F1','/F10','/F11','/F2','/F3','/F4','/F5','/F6','/F7','/F8','/F9','/FS','/FT','/Ff','/Filespec','/Fit','/FitH','/Font','/FontBBox','/FontFile2','/FontMatrix','/FontStretch','/FontWeight','/Form','/FormType','/FunctionType','/G','/GS0','/GS1','/GS2','/Gamma','/GoTo','/Group','/H','/Helv','/Helvetica','/I','/ICCBased','/ID','/IF','/Identity','/Im0','/Im1','/Im2','/Im6','/Im7','/Im9','/ImageB','/ImageC','/ImageI','/ImageMask','/Indexed','/Info','/J','/JavaScript','/K','/Keywords','/Kids','/L','/L2R','/LZWDecode','/Lang','/Last','/Launch','/Leading','/Length1','/Linearized','/M','/MK','/MacRomanEncoding','/Marked','/Matrix','/MaxWidth','/MediaBox','/MissingWidth','/ModDate','/N','/Name','/Names','/Next','/None','/Normal','/O','/OCGs','/ON','/OP','/OPM','/ObjStm','/OneColumn','/OpenAction','/Outlines','/P','/PageLabels','/PageLayout','/PageMode','/Pages','/Parent','/PieceInfo','/Predictor','/Prev','/ProcSet','/Producer','/Properties','/Q','/R10','/R7','/R8','/R9','/Rect','/Resources','/Root','/Rotate','/S','/SA','/SM','/SMask','/Size','/StemH','/StemV','/StructParents','/StructTreeRoot','/Subj','/Subject','/Subtype','/Supplement','/T','/T1','/TP','/TT0','/TT1','/TT2','/TT4','/TU','/Tabs','/Text','/Threads','/Times','/TimesNewRomanPSMT','/Title','/ToUnicode','/Transparency','/Trapped','/TrimBox','/TrueType','/Type','/Type0','/Type1','/Type1C','/U','/URI','/UseOutlines','/V','/Version','/ViewerPreferences','/W','/Widget','/Width','/Widths','/WinAnsiEncoding','/X','/XHeight','/XObject','/XRef','/XRefStm','/XYZ','/Y','/Z','/a','/acute','/alpha','/arrowright','/asteriskmath','/at','/b','/beta','/bullet','/ca','/d','/dieresis','/e','/element','/endash','/f','/ff','/ffi','/fi','/fl','/g','/h','/i','/iX','/j','/k','/l','/less','/lessequal','/lslash','/minus','/mu','/multiply','/n','/o','/op','/p','/pdf','/pdftk','/pdfx','/percent','/periodcentered','/photoshop','/pi','/plus','/prime','/q','/question','/quotedblright','/quoteright','/r','/ring','/schema','/semicolon','/sigma','/slash','/space','/t','/thorn','/u','/v','/w','/www','/x','/xap','/xapMM','/xfa','/xmpMM','/y','/ydieresis','/z','/zcaron','/zero','/ÃŸ','After last EOF','obj','startxref','stream','xref']
        Mins = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,2,0,1,0]
        Diff = [208,6,118,246,633,228,714,220,190,230,213,1490,54,75,7,146,26,71,6,8,1477,39,193,41,75,45,35,241,40,23,75,1477,430,206,125,1477,19,1296,293,414,75,535,11,11,670,90,38,77,1088,216,6,1779,66,23,38,45,584,94,685,51,398,584,61,770,579,685,430,192,17,12,859,22,1507,906,88,161,187,284,160,84,83,111,66,38,5,83,80,118,604,1606,1505,430,79,430,40,40,7387,427,617,206,679,408,269,12,1475,627,1820,176,39,786,140,68,27,2321,584,91,60,32,32,32,582,229,229,580,286,68,252,149,2764,18,65,205,7,522,206,58,72,48,79,20,259,106,62,24,1066,101,584,74,38,1139,822,119,138,75,527,2195,14,11,75,150,588,12,12,14,3047,12,12,9,75,1572,1066,218,156,833,38,115,261,100,221,198,222,1477,1649,66,584,4445,75,33,304,399,100,131,160,24,6,18,7387,124,1140,233,73,121,117,408,124,62,160,408,5,185,11,174,143,200,11,75,92,7400,72,130,77,199,2427,7,1138,41,7,1790,146,822,430,430,845,131,7391,47,24,7173,213,247,229,97,11,7,9,97,231,9,148,224,237,95,266,13,99,213,29,11,109,97,258,235,217,12,284,349,236,95,95,7,29,95,25,312,296,168,228,234,5,133,95,97,347,95,97,15,193,95,99,99,225,97,5,99,7,103,189,194,22,298,309,220,359,263,1231,127,6,1117,184,95,180,22,105,250,16457266,8942,68,7435,46]
        try:
            F,V = extractFeatures(self.filename1)        
            Values = []
            for i in range(len(Featurelist)):
                if Featurelist[i] in F:        
                    Values.append(V[F.index(Featurelist[i])])
                else:
                    Values.append(-1)                
            for i in range (len(tobeNumerical)):
                Values[Featurelist.index(tobeNumerical[i])]=(Values[Featurelist.index(tobeNumerical[i])] - Mins[i])/Diff[i]
            Y_pred_NN = mygetLabel(Values)
        except Exception as e:
            Y_pred_NN = 1
        per = Y_pred_NN[0]
        return per
        #text_file = open("result.txt", "w")
        #text_file.write(str(Y_pred_NN))
        #text_file.close()
#%%
import sys
import zipfile
import os
import urllib2
class cBinaryFile:
    def __init__(self, file):
        self.file = file
        if file == '':
            self.infile = sys.stdin
        elif file.lower().startswith('http://') or file.lower().startswith('https://'):
            try:
                if sys.hexversion >= 0x020601F0:
                    self.infile = urllib2.urlopen(file, timeout=5)
                else:
                    self.infile = urllib2.urlopen(file)
            except urllib2.HTTPError:
                print('Error accessing URL %s' % file)
                print(sys.exc_info()[1])
                sys.exit()
        elif file.lower().endswith('.zip'):
            try:
                self.zipfile = zipfile.ZipFile(file, 'r')
                self.infile = self.zipfile.open(self.zipfile.infolist()[0], 'r', C2BIP3('infected'))
            except:
                print('Error opening file %s' % file)
                print(sys.exc_info()[1])
                sys.exit()
        else:
            try:
                self.infile = open(file, 'rb')
            except:
                print('Error opening file %s' % file)
                print(sys.exc_info()[1])
                sys.exit()
        self.ungetted = []

    def byte(self):
        if len(self.ungetted) != 0:
            return self.ungetted.pop()
        inbyte = self.infile.read(1)
        if not inbyte or inbyte == '':
            self.infile.close()
            return None
        return ord(inbyte)

    def bytes(self, size):
        if size <= len(self.ungetted):
            result = self.ungetted[0:size]
            del self.ungetted[0:size]
            return result
        inbytes = self.infile.read(size - len(self.ungetted))
        if inbytes == '':
            self.infile.close()
        if type(inbytes) == type(''):
            result = self.ungetted + [ord(b) for b in inbytes]
        else:
            result = self.ungetted + [b for b in inbytes]
        self.ungetted = []
        return result

    def unget(self, byte):
        self.ungetted.append(byte)

    def ungets(self, bytes):
        bytes.reverse()
        self.ungetted.extend(bytes)


class cEntropy:
    def __init__(self):
        self.allBucket = [0 for i in range(0, 256)]
        self.streamBucket = [0 for i in range(0, 256)]

    def add(self, byte, insideStream):
        self.allBucket[byte] += 1
        if insideStream:
            self.streamBucket[byte] += 1

    def removeInsideStream(self, byte):
        if self.streamBucket[byte] > 0:
            self.streamBucket[byte] -= 1
class cPDFEOF:
    def __init__(self):
        self.token = ''
        self.cntEOFs = 0

    def parse(self, char):
        if self.cntEOFs > 0:
            self.cntCharsAfterLastEOF += 1
        if self.token == '' and char == '%':
            self.token += char
            return
        elif self.token == '%' and char == '%':
            self.token += char
            return
        elif self.token == '%%' and char == 'E':
            self.token += char
            return
        elif self.token == '%%E' and char == 'O':
            self.token += char
            return
        elif self.token == '%%EO' and char == 'F':
            self.token += char
            return
        elif self.token == '%%EOF' and (char == '\n' or char == '\r' or char == ' ' or char == '\t'):
            self.cntEOFs += 1
            self.cntCharsAfterLastEOF = 0
            if char == '\n':
                self.token = ''
            else:
                self.token += char
            return
        elif self.token == '%%EOF\r':
            if char == '\n':
                self.cntCharsAfterLastEOF = 0
            self.token = ''
        else:
            self.token = ''

def FindPDFHeaderRelaxed(oBinaryFile):
    bytes = oBinaryFile.bytes(1024)
    index = ''.join([chr(byte) for byte in bytes]).find('%PDF')
    if index == -1:
        oBinaryFile.ungets(bytes)
        return ([], None)
    for endHeader in range(index + 4, index + 4 + 10):
        if bytes[endHeader] == 10 or bytes[endHeader] == 13:
            break
    oBinaryFile.ungets(bytes[endHeader:])
    return (bytes[0:endHeader], ''.join([chr(byte) for byte in bytes[index:endHeader]]))

def Hexcode2String(char):
    if type(char) == int:
        return '#%02x' % char
    else:
        return char

def SwapCase(char):
    if type(char) == int:
        return ord(chr(char).swapcase())
    else:
        return char.swapcase()

def HexcodeName2String(hexcodeName):
    return ''.join(map(Hexcode2String, hexcodeName))

def SwapName(wordExact):
    return map(SwapCase, wordExact)

def UpdateWords(word, wordExact, slash, words, hexcode, allNames, lastName, insideStream, oEntropy, fOut):
    if word != '':
        if slash + word in words:
            words[slash + word][0] += 1
            if hexcode:
                words[slash + word][1] += 1
        elif slash == '/' and allNames:
            words[slash + word] = [1, 0]
            if hexcode:
                words[slash + word][1] += 1
        if slash == '/':
            lastName = slash + word
        if slash == '':
            if word == 'stream':
                insideStream = True
            if word == 'endstream':
                if insideStream == True and oEntropy != None:
                    for char in 'endstream':
                        oEntropy.removeInsideStream(ord(char))
                insideStream = False
        if fOut != None:
            if slash == '/' and '/' + word in ('/JS', '/JavaScript', '/AA', '/OpenAction', '/JBIG2Decode', '/RichMedia', '/Launch'):
                wordExactSwapped = HexcodeName2String(SwapName(wordExact))
                fOut.write(C2BIP3(wordExactSwapped))
                print('/%s -> /%s' % (HexcodeName2String(wordExact), wordExactSwapped))
            else:
                fOut.write(C2BIP3(HexcodeName2String(wordExact)))
    return ('', [], False, lastName, insideStream)

class cCVE_2009_3459:
    def __init__(self):
        self.count = 0

    def Check(self, lastName, word):
        if (lastName == '/Colors' and word.isdigit() and int(word) > 2^24): # decided to alert when the number of colors is expressed with more than 3 bytes
            self.count += 1



def PDFiD(file, allNames=False, extraData=False, disarm=False, force=False):
    
    word = ''
    wordExact = []
    hexcode = False
    lastName = ''
    insideStream = False
    keywords = ['obj',
                'endobj',
                'stream',
                'endstream',
                'xref',
                'trailer',
                'startxref',
                '/Page',
                '/Encrypt',
                '/ObjStm',
                '/JS',
                '/JavaScript',
                '/AA',
                '/OpenAction',
                '/AcroForm',
                '/JBIG2Decode',
                '/RichMedia',
                '/Launch',
                '/EmbeddedFile',
                '/XFA',
               ]
    words = {}
    dates = []
    for keyword in keywords:
        words[keyword] = [0, 0]
    slash = ''
    import xml.dom.minidom

    xmlDoc = xml.dom.minidom.getDOMImplementation().createDocument(None, 'PDFiD', None)

    oEntropy = None
    oPDFEOF = None
    oCVE_2009_3459 = cCVE_2009_3459()
    try:
        attIsPDF = xmlDoc.createAttribute('IsPDF')
        xmlDoc.documentElement.setAttributeNode(attIsPDF)
        oBinaryFile = cBinaryFile(file)
        if extraData:
            #oPDFDate = cPDFDate()
            oEntropy = cEntropy()
            oPDFEOF = cPDFEOF()
        (bytesHeader, pdfHeader) = FindPDFHeaderRelaxed(oBinaryFile)
        if disarm:
            (pathfile, extension) = os.path.splitext(file)
            fOut = open(pathfile + '.disarmed' + extension, 'wb')
            for byteHeader in bytesHeader:
                fOut.write(C2BIP3(chr(byteHeader)))
        else:
            fOut = None
        if oEntropy != None:
            for byteHeader in bytesHeader:
                oEntropy.add(byteHeader, insideStream)
        if pdfHeader == None and not force:
            attIsPDF.nodeValue = 'False'
            return xmlDoc
        else:
            if pdfHeader == None:
                attIsPDF.nodeValue = 'False'
                pdfHeader = ''
            else:
                attIsPDF.nodeValue = 'True'
            att = xmlDoc.createAttribute('Header')
            att.nodeValue = repr(pdfHeader[0:10]).strip("'")
            xmlDoc.documentElement.setAttributeNode(att)
        byte = oBinaryFile.byte()
        while byte != None:
            char = chr(byte)
            charUpper = char.upper()
            if charUpper >= 'A' and charUpper <= 'Z' or charUpper >= '0' and charUpper <= '9':
                word += char
                wordExact.append(char)
            elif slash == '/' and char == '#':
                d1 = oBinaryFile.byte()
                if d1 != None:
                    d2 = oBinaryFile.byte()
                    if d2 != None and (chr(d1) >= '0' and chr(d1) <= '9' or chr(d1).upper() >= 'A' and chr(d1).upper() <= 'F') and (chr(d2) >= '0' and chr(d2) <= '9' or chr(d2).upper() >= 'A' and chr(d2).upper() <= 'F'):
                        word += chr(int(chr(d1) + chr(d2), 16))
                        wordExact.append(int(chr(d1) + chr(d2), 16))
                        hexcode = True
                        if oEntropy != None:
                            oEntropy.add(d1, insideStream)
                            oEntropy.add(d2, insideStream)
                        if oPDFEOF != None:
                            oPDFEOF.parse(d1)
                            oPDFEOF.parse(d2)
                    else:
                        oBinaryFile.unget(d2)
                        oBinaryFile.unget(d1)
                        (word, wordExact, hexcode, lastName, insideStream) = UpdateWords(word, wordExact, slash, words, hexcode, allNames, lastName, insideStream, oEntropy, fOut)
                        if disarm:
                            fOut.write(C2BIP3(char))
                else:
                    oBinaryFile.unget(d1)
                    (word, wordExact, hexcode, lastName, insideStream) = UpdateWords(word, wordExact, slash, words, hexcode, allNames, lastName, insideStream, oEntropy, fOut)
                    if disarm:
                        fOut.write(C2BIP3(char))
            else:
                oCVE_2009_3459.Check(lastName, word)

                (word, wordExact, hexcode, lastName, insideStream) = UpdateWords(word, wordExact, slash, words, hexcode, allNames, lastName, insideStream, oEntropy, fOut)
                if char == '/':
                    slash = '/'
                else:
                    slash = ''
                if disarm:
                    fOut.write(C2BIP3(char))

            if oEntropy != None:
                oEntropy.add(byte, insideStream)

            if oPDFEOF != None:
                oPDFEOF.parse(char)

            byte = oBinaryFile.byte()
        (word, wordExact, hexcode, lastName, insideStream) = UpdateWords(word, wordExact, slash, words, hexcode, allNames, lastName, insideStream, oEntropy, fOut)

        if byte == None and oPDFEOF != None:
            if oPDFEOF.token == '%%EOF':
                oPDFEOF.cntEOFs += 1
                oPDFEOF.cntCharsAfterLastEOF = 0
                oPDFEOF.token = ''

    except:
        print("damage")
        return

    if disarm:
        fOut.close()

    attEntropyAll = xmlDoc.createAttribute('TotalEntropy')
    xmlDoc.documentElement.setAttributeNode(attEntropyAll)
    attCountAll = xmlDoc.createAttribute('TotalCount')
    xmlDoc.documentElement.setAttributeNode(attCountAll)
    attEntropyStream = xmlDoc.createAttribute('StreamEntropy')
    xmlDoc.documentElement.setAttributeNode(attEntropyStream)
    attCountStream = xmlDoc.createAttribute('StreamCount')
    xmlDoc.documentElement.setAttributeNode(attCountStream)
    attEntropyNonStream = xmlDoc.createAttribute('NonStreamEntropy')
    xmlDoc.documentElement.setAttributeNode(attEntropyNonStream)
    attCountNonStream = xmlDoc.createAttribute('NonStreamCount')
    xmlDoc.documentElement.setAttributeNode(attCountNonStream)

    attCountEOF = xmlDoc.createAttribute('CountEOF')
    xmlDoc.documentElement.setAttributeNode(attCountEOF)
    attCountCharsAfterLastEOF = xmlDoc.createAttribute('CountCharsAfterLastEOF')
    xmlDoc.documentElement.setAttributeNode(attCountCharsAfterLastEOF)
    if oPDFEOF != None:
        attCountEOF.nodeValue = '%d' % oPDFEOF.cntEOFs
        attCountCharsAfterLastEOF.nodeValue = '%d' % oPDFEOF.cntCharsAfterLastEOF
    else:
        attCountEOF.nodeValue = ''
        attCountCharsAfterLastEOF.nodeValue = ''

    eleKeywords = xmlDoc.createElement('Keywords')
    xmlDoc.documentElement.appendChild(eleKeywords)
    for keyword in keywords:
        eleKeyword = xmlDoc.createElement('Keyword')
        eleKeywords.appendChild(eleKeyword)
        att = xmlDoc.createAttribute('Name')
        att.nodeValue = keyword
        eleKeyword.setAttributeNode(att)
        att = xmlDoc.createAttribute('Count')
        att.nodeValue = str(words[keyword][0])
        eleKeyword.setAttributeNode(att)
        att = xmlDoc.createAttribute('HexcodeCount')
        att.nodeValue = str(words[keyword][1])
        eleKeyword.setAttributeNode(att)
    eleKeyword = xmlDoc.createElement('Keyword')
    eleKeywords.appendChild(eleKeyword)
    att = xmlDoc.createAttribute('Name')
    att.nodeValue = '/Colors > 2^24'
    eleKeyword.setAttributeNode(att)
    att = xmlDoc.createAttribute('Count')
    att.nodeValue = str(oCVE_2009_3459.count)
    eleKeyword.setAttributeNode(att)
    att = xmlDoc.createAttribute('HexcodeCount')
    att.nodeValue = str(0)
    eleKeyword.setAttributeNode(att)
    if allNames:
        keys = sorted(words.keys())
        for word in keys:
            if not word in keywords:
                eleKeyword = xmlDoc.createElement('Keyword')
                eleKeywords.appendChild(eleKeyword)
                att = xmlDoc.createAttribute('Name')
                att.nodeValue = word
                eleKeyword.setAttributeNode(att)
                att = xmlDoc.createAttribute('Count')
                att.nodeValue = str(words[word][0])
                eleKeyword.setAttributeNode(att)
                att = xmlDoc.createAttribute('HexcodeCount')
                att.nodeValue = str(words[word][1])
                eleKeyword.setAttributeNode(att)
    eleDates = xmlDoc.createElement('Dates')
    xmlDoc.documentElement.appendChild(eleDates)
    dates.sort(key=lambda x: x[0])
    for date in dates:
        eleDate = xmlDoc.createElement('Date')
        eleDates.appendChild(eleDate)
        att = xmlDoc.createAttribute('Value')
        att.nodeValue = date[0]
        eleDate.setAttributeNode(att)
        att = xmlDoc.createAttribute('Name')
        att.nodeValue = date[1]
        eleDate.setAttributeNode(att)
    return xmlDoc



def extractFeatures(filename):   
    import argparse
    import xml.dom.minidom
    oParser = argparse.ArgumentParser(description='something')
    oParser.add_argument('-a', '--all', action='store_true', default=True, help='display all the names')
    oParser.add_argument('-e', '--extra', action='store_true', default=True, help='display extra data, like dates')
    oParser.add_argument('-f', '--force', action='store_true', default=True, help='force the scan of the file, even without proper %PDF header')
    oParser.add_argument('-d', '--disarm', action='store_true', default=False, help='disable JavaScript and auto launch')
    oParser.add_argument('-m', '--minimumscore', type=float, default=0.0, help='minimum score for plugin results output')
    options = oParser.parse_args()
    xmlDoc = PDFiD(filename, options.all, options.extra, options.disarm, options.force)    
    Values = []
    Features = []
    for node in xmlDoc.documentElement.getElementsByTagName('Keywords')[0].childNodes:
        Features.append(node.getAttribute('Name'))        
        Values.append(int(node.getAttribute('Count')))        
    if xmlDoc.documentElement.getAttribute('CountCharsAfterLastEOF') != '':
        Features.append('After last EOF')
        Values.append(int(xmlDoc.documentElement.getAttribute('CountCharsAfterLastEOF')))
        
    for node in xmlDoc.documentElement.getElementsByTagName('Dates')[0].childNodes:
        Features.append(node.getAttribute('Value'))
        Values.append(node.getAttribute('Name'))        


    return Features, Values

#%%
def mygetLabel(Values):
    intercepts_ = [([0.84081887,0.62713374,0.07236525,-3.99475676,0.1136401,1.67214417,0.94038081,-0.90008814,1.58406075,1.51856386]),([1.27931654,-4.59475505,1.82865619,-1.90580673,-3.87554027]),([14.64167695])]
    coefs_ = [([[5.03484709e+00,-2.39206256e+00,-2.33021529e+00,2.96041553e+00,-4.80580510e+00,6.87828619e-01,-3.64911656e+00,-3.02119340e+00,4.14781166e+00,-2.38737766e+00],[2.64113412e+00,-6.95434779e+00,-1.29473214e+00,-1.88984100e+00,-2.67306234e+00,2.11019873e-01,-1.68496440e+00,-1.81075734e+00,2.49766237e+00,1.00963325e+00],[2.97301847e-01,-3.18133284e-02,-1.44625978e-01,-1.86518338e+00,-1.88189969e-01,1.04916064e-01,-2.63701749e-01,-2.26201944e-01,1.66810767e-01,5.29974067e+00],[4.24902368e+00,-2.30918307e+00,-1.86022017e+00,2.00635568e+00,-4.03601168e+00,6.00144344e-01,-3.05096303e+00,-2.52403483e+00,3.50771377e+00,-3.36808543e+00],[1.63644156e+00,-7.41020567e-01,-7.30816024e-01,1.03727226e+00,-1.52785058e+00,2.16675444e-01,-1.05474776e+00,-9.55396847e-01,1.24972132e+00,5.73611924e+00],[4.96566197e+00,-2.34134057e+00,-2.28703935e+00,2.16965761e+00,-4.72228322e+00,6.46092535e-01,-3.57541275e+00,-3.04757343e+00,4.19141094e+00,-1.39739308e+00],[1.42286684e+00,-7.77447259e-01,-6.39399767e-01,6.04671796e-01,-1.47391335e+00,2.11804759e-01,-1.03465833e+00,-8.95741213e-01,1.31238347e+00,-4.80070929e-01],[4.74161341e+00,-2.32683346e+00,-2.13959694e+00,2.56766012e+00,-4.41135794e+00,6.32986233e-01,-3.27940912e+00,-2.79423668e+00,3.89045753e+00,8.65559027e-01],[5.36104774e+00,-2.43632300e+00,-2.32310371e+00,3.46831902e+00,-5.00379226e+00,8.11396114e-01,-3.79865905e+00,-3.07290829e+00,4.39493214e+00,-9.98015830e-01],[4.16096784e+00,-2.00053660e+00,-1.90363500e+00,9.46021621e-01,-4.00500117e+00,5.71643587e-01,-2.93384324e+00,-2.52401679e+00,3.44856480e+00,6.40903899e+00],[4.43719076e+00,-2.33039066e+00,-1.95605750e+00,1.94763896e+00,-4.14520789e+00,6.45590097e-01,-3.23247753e+00,-2.61572694e+00,3.71892848e+00,6.22881840e-01],[1.88263492e+00,-1.30997613e+00,-8.21882745e-01,5.32056339e-01,-1.93268787e+00,3.24805297e-01,-1.35050072e+00,-1.13899490e+00,1.70195871e+00,-1.92782766e+00],[4.73448720e-02,-7.86323432e-02,-1.24819504e-01,-7.24482585e-01,-6.74998473e-02,2.23766341e-02,-9.90069274e-02,-2.19418711e-02,3.96469449e-02,4.54927103e+00],[9.65524577e-01,-6.17719466e-01,-4.24734958e-01,3.71065461e-01,-8.81706118e-01,-1.79489451e-02,-4.93487330e-01,-7.14117745e-01,1.10311784e+00,-4.25642257e-01],[4.47239800e-01,-2.46520694e-01,-2.59074056e-01,-2.06352777e+00,-4.74767123e-01,5.80432010e-02,-3.36008773e-01,-2.27600644e-01,3.64086813e-01,6.46185322e-01],[1.80748451e-01,-2.59444808e-02,-1.00752724e-01,1.64979493e-01,-2.79717252e-01,6.71026625e-02,-2.24951816e-01,-1.34209453e-01,2.73990106e-01,-1.88959509e-01],[1.75357523e-01,5.66681042e-01,-8.02297946e-02,-1.10014234e-01,-2.63508504e-01,1.55313269e-01,-2.67129338e-01,-8.27081416e-02,1.83356332e-01,-3.09625315e-01],[1.60501277e+00,-4.92002752e-01,-7.10072024e-01,2.59079920e-01,-1.49001277e+00,2.95085244e-01,-1.16991698e+00,-9.80310830e-01,1.29671757e+00,1.68322224e+00],[-2.85917279e+00,1.14723776e-01,1.37471163e+00,-2.98797822e+00,2.87480365e+00,-2.72955840e-01,1.90837699e+00,1.68460752e+00,-2.28139285e+00,4.83009563e+00],[-5.52382487e+00,1.64800347e+00,2.36753208e+00,-4.32789082e+00,5.03091045e+00,-9.47787312e-01,3.73745256e+00,3.02124402e+00,-4.21836847e+00,3.78063126e+00],[2.20096106e-01,-3.85117051e-02,-4.36945499e-03,-5.88626965e-01,-1.56875536e-01,3.18840394e-02,-9.52973182e-02,-7.65062763e-02,1.80024418e-01,-8.89633114e-01],[2.22126105e+00,-1.25199237e+00,-1.04613655e+00,9.40651007e-01,-2.16210586e+00,3.46499478e-01,-1.68783350e+00,-1.24650209e+00,1.87504154e+00,-6.61991057e+00],[2.37718141e+00,-1.43472483e+00,-1.12997265e+00,1.30546696e+00,-2.28026673e+00,4.85901655e-01,-1.73436650e+00,-1.34613931e+00,2.00073647e+00,-2.91220084e+00],[2.99454067e+00,-9.45734674e-01,-1.26789983e+00,2.59481870e+00,-2.77263660e+00,5.41550033e-01,-2.25356186e+00,-1.68209195e+00,2.32508385e+00,-1.18982926e+00],[1.86787181e+00,-1.84993204e+00,-8.15126325e-01,1.28917090e-01,-1.70101111e+00,2.75092762e-01,-1.41017677e+00,-1.09952252e+00,1.50490537e+00,3.83407349e-01],[3.59185575e-01,1.41906499e+00,-1.01509350e-01,-2.45222721e+00,-2.82986949e-01,8.54231100e-02,-2.42035540e-01,-1.44691687e-01,2.88210017e-01,2.28669943e+00],[5.88296547e+00,-2.47813383e+00,-2.55110292e+00,4.61776024e+00,-5.40111160e+00,8.13192809e-01,-4.10376474e+00,-3.47265730e+00,4.80934491e+00,-7.93421422e-01],[5.65539253e+00,-2.75280360e+00,-2.51127538e+00,3.29084174e+00,-5.25270691e+00,8.84276047e-01,-4.11133142e+00,-3.35603629e+00,4.62127120e+00,-1.44101426e+00],[1.09376562e+00,-3.43980859e-01,-4.47858162e-01,2.09761297e-01,-1.05784510e+00,2.21166445e-01,-7.51820193e-01,-5.74684715e-01,8.67909661e-01,-1.40406171e-01],[1.25507698e+00,-3.82543172e-01,-5.39618706e-01,-1.25282749e-01,-1.18370094e+00,1.47873681e-01,-9.26442148e-01,-7.78141260e-01,1.07582393e+00,1.49850833e+00],[1.69099620e+00,-8.91599311e-01,-7.07779177e-01,1.16971689e+00,-1.61768788e+00,1.25261085e-01,-1.06440372e+00,-1.12663736e+00,1.59673078e+00,-1.36375054e+00],[6.45247044e-01,-1.43370106e-01,-2.91132723e-01,1.06321753e-01,-5.84186759e-01,1.02590272e-01,-3.87429701e-01,-3.69413191e-01,4.10856542e-01,1.50392780e-01],[1.24175250e+00,-4.41762547e-01,-5.90510770e-01,5.61555792e-01,-1.15944510e+00,2.16006451e-01,-9.59778980e-01,-6.90288713e-01,9.77891736e-01,8.51111990e-01],[8.41374121e+00,-3.25638722e+00,-3.79595897e+00,3.72436322e+00,-7.88873883e+00,1.30441069e+00,-6.16370104e+00,-4.88554660e+00,6.90414223e+00,-2.34665824e+00],[1.53761474e+00,-1.26148420e+00,-6.01063536e-01,2.55958087e-01,-1.43084303e+00,2.29410089e-01,-1.01531791e+00,-8.39208455e-01,1.21203662e+00,-7.41708200e-01],[1.97116521e+00,-1.42961344e+00,-9.11443418e-01,4.69325332e-01,-1.81098096e+00,2.66603957e-01,-1.33787392e+00,-1.18810447e+00,1.69410937e+00,-2.01392540e+00],[-8.47936607e-01,4.81575783e-01,4.30734168e-01,-4.25488512e-01,8.48873896e-01,-6.57231270e-02,6.06812241e-01,5.64303145e-01,-8.42183860e-01,-1.28407512e+00],[2.72039970e+00,-1.33075592e+00,-1.27330685e+00,4.50810503e-01,-2.62324245e+00,4.15202544e-01,-1.93046945e+00,-1.57702387e+00,2.24209103e+00,2.31909769e-01],[7.91082720e-01,-2.65228010e-01,-2.75537568e-01,-5.58377363e-02,-7.77002018e-01,1.07398130e-01,-5.44872891e-01,-4.53598605e-01,5.49342254e-01,1.02206756e+00],[6.62017070e-01,-3.61425862e-01,-3.47643248e-01,2.93738145e-01,-6.54151555e-01,1.27310364e-01,-5.08511434e-01,-3.94698245e-01,6.13872502e-01,-9.40647697e-02],[2.10219670e+00,-1.06815407e+00,-9.80739654e-01,1.27252047e+00,-1.94863419e+00,2.31855711e-01,-1.36459457e+00,-1.34741741e+00,1.83246057e+00,-2.03895576e+00],[1.00309134e+00,-3.40095691e-01,-4.20404542e-01,6.87800087e-01,-9.41167845e-01,1.67633797e-01,-7.18815912e-01,-6.06347912e-01,8.67211420e-01,-7.95595476e-01],[1.11273729e+01,-4.44799998e+00,-4.97138131e+00,1.22630108e+00,-1.03349071e+01,1.69601445e+00,-8.10249810e+00,-6.32799708e+00,8.77213379e+00,2.19796980e+00],[7.87636954e+00,-3.06915608e+00,-3.45245262e+00,3.13137414e+00,-7.23208907e+00,1.26065827e+00,-5.58858294e+00,-4.52843294e+00,6.19848497e+00,-2.41626933e+00],[6.97081029e-01,-5.66868870e-01,-3.04997020e-01,5.27746628e-01,-5.80700406e-01,1.38966666e-01,-4.08457494e-01,-3.67608875e-01,5.37896841e-01,-6.53621747e-01],[2.00910640e+00,-2.52386021e+00,-9.55484542e-01,3.71404911e+00,-2.01046176e+00,1.23739796e-01,-1.18069067e+00,-1.52543442e+00,2.06022229e+00,-4.67853979e+00],[-6.72301585e-02,2.12862070e-01,-2.59410367e-02,-2.61226931e+00,9.63908535e-02,2.39658636e-02,8.66449443e-02,-5.01729508e-02,2.25670632e-02,3.30957541e+00],[1.12096660e+01,-4.39594829e+00,-4.92491229e+00,4.28696794e+00,-1.02558733e+01,1.73720184e+00,-8.04660684e+00,-6.35950036e+00,8.86559593e+00,1.89511501e+00],[3.45372768e+00,-1.64168015e+00,-1.54549697e+00,2.03119262e+00,-3.27521304e+00,5.24557951e-01,-2.50256007e+00,-2.13511424e+00,2.87330031e+00,-7.01610894e-01],[7.02327307e-01,-7.02105224e-01,-3.35132191e-01,6.62119442e-01,-6.99163188e-01,1.29018169e-01,-3.81264333e-01,-4.26636812e-01,7.60447511e-01,-1.57009548e+00],[7.45050248e-02,-8.91216981e-02,-8.73835120e-02,-7.17438749e-01,-1.10095421e-01,5.22954836e-03,-4.91485801e-02,-1.23462550e-01,1.35556735e-01,2.70761701e+00],[8.10693877e-01,-4.03815615e-01,-4.22359072e-01,5.73499204e-01,-7.23465252e-01,1.33553688e-01,-5.71726856e-01,-5.13469414e-01,6.53530558e-01,-6.29454734e-02],[2.63809084e+00,-3.49840671e-01,-1.02265003e+00,-2.52202379e+00,-2.41006334e+00,3.52055824e-01,-1.92204578e+00,-1.57536626e+00,2.19010426e+00,4.82443343e+00],[6.38509728e-01,1.30862651e-02,-2.02271308e-01,-3.11739691e+00,-5.20303748e-01,2.68599471e-01,-4.47190390e-01,-3.19926803e-01,3.30853154e-01,-3.73049670e-01],[3.44087456e+00,5.50813652e-01,-1.35291615e+00,5.80017841e+00,-3.08046703e+00,5.11955227e-01,-2.40355129e+00,-1.79619765e+00,2.61356373e+00,-6.27577605e+00],[2.74791299e+00,-8.79605945e-03,-1.07702512e+00,4.94449483e-01,-2.54279190e+00,3.68704363e-01,-1.89102489e+00,-1.48706100e+00,2.21852223e+00,2.75428371e+00],[1.80920345e+00,-1.28566416e+00,-8.24280192e-01,1.20119531e+00,-1.79336873e+00,2.65677148e-01,-1.32572705e+00,-1.13583853e+00,1.69207382e+00,-1.15073921e+00],[2.93354311e-01,-3.86844090e-02,-8.62232741e-02,2.21494197e-01,-2.68120162e-01,3.15859974e-02,-2.49443442e-01,-1.67484262e-01,2.66007850e-01,-1.52691842e+00],[1.94495691e+00,-8.41189453e-01,-8.04440360e-01,1.22427876e+00,-1.72989754e+00,2.71505758e-01,-1.30566533e+00,-1.12729116e+00,1.48491583e+00,-1.23182787e+00],[2.79562227e+00,-1.03962008e+00,-1.19830912e+00,1.57868102e+00,-2.65068690e+00,4.15399736e-01,-2.08857850e+00,-1.62030596e+00,2.13818278e+00,-3.07607403e+00],[1.29312222e+00,-4.07472375e-01,-6.17958169e-01,5.25576934e-01,-1.21590170e+00,2.56239181e-01,-8.94730597e-01,-7.02538333e-01,9.48624852e-01,-1.05864098e+00],[1.20832721e+00,-6.81392099e-01,-5.25223676e-01,8.53874511e-01,-1.20729664e+00,2.59425312e-01,-9.10017951e-01,-7.82750316e-01,1.01324972e+00,-6.24016981e-01],[2.53343675e+00,-1.04609579e+00,-1.20185252e+00,6.05375471e-01,-2.37075833e+00,3.99008027e-01,-1.86794749e+00,-1.49069793e+00,2.13386032e+00,-1.61424641e+00],[2.50853717e+00,-1.61506806e+00,-1.05420247e+00,1.35722601e+00,-2.30095136e+00,3.18957702e-01,-1.76482332e+00,-1.52362853e+00,2.06206056e+00,-2.03160390e+00],[9.35594513e-01,-5.20681660e-01,-4.69465689e-01,7.90043578e-01,-9.42639300e-01,6.91365225e-02,-7.42021054e-01,-6.69622489e-01,8.51954493e-01,-1.86156155e+00],[1.66581155e+00,-8.27057368e-01,-7.00320415e-01,1.13156070e+00,-1.49515470e+00,2.35615325e-01,-1.19345719e+00,-1.03753547e+00,1.37920843e+00,-2.96364466e-01],[1.96062366e+00,-7.68892290e-01,-9.24257242e-01,1.05186745e+00,-1.87861956e+00,3.56062611e-01,-1.37943364e+00,-1.19541214e+00,1.64151153e+00,7.08854241e-01],[7.00450968e+00,-3.57563602e+00,-3.13632109e+00,3.91388322e+00,-6.51936299e+00,1.14058346e+00,-5.04087990e+00,-4.20035259e+00,5.77022653e+00,-3.95174127e-01],[-3.31689660e-01,8.62256962e-02,2.09013707e-01,-1.66254640e+00,3.58195967e-01,1.92108407e-01,2.59513902e-01,3.37573425e-01,-4.87316614e-01,6.43935092e-01],[-6.75737331e+00,3.60464155e+00,3.08753336e+00,-4.33495366e+00,6.45251500e+00,-1.01885109e+00,4.86136285e+00,4.20256570e+00,-5.92505614e+00,-4.44233268e-01],[2.82031094e+00,-1.14450085e+00,-1.25604271e+00,1.26023601e+00,-2.69525619e+00,4.62355694e-01,-2.03135876e+00,-1.68087785e+00,2.29303871e+00,2.88995156e-01],[7.70655969e-01,-5.87338346e-01,-4.44334114e-01,4.42480751e-01,-8.39177091e-01,3.59615372e-02,-5.34579665e-01,-6.36382349e-01,9.68418575e-01,-5.31116413e-01],[1.80737296e+00,-7.23494887e-01,-7.94284653e-01,1.37552194e+00,-1.70728209e+00,2.82136044e-01,-1.23019175e+00,-1.13913518e+00,1.50230119e+00,-2.07248709e+00],[8.16144079e-01,-3.19039514e-01,-3.04676402e-01,1.66023010e-01,-7.23263982e-01,1.56329291e-01,-5.20828024e-01,-4.39159588e-01,6.89904698e-01,-2.09092936e+00],[1.72465050e+00,-8.81680917e-01,-7.76976438e-01,1.01474206e+00,-1.65266480e+00,2.68614124e-01,-1.12880820e+00,-1.04455469e+00,1.42028449e+00,-1.06002811e+00],[1.03130241e+00,-4.58640496e-01,-3.91153457e-01,4.02810859e-01,-9.62374940e-01,2.34836319e-01,-7.66992386e-01,-5.65779120e-01,8.11396678e-01,1.21452891e-01],[2.32458273e+00,-8.14238138e-01,-1.07945564e+00,1.54025481e-01,-2.27528504e+00,3.50434671e-01,-1.68406483e+00,-1.36268092e+00,1.97649461e+00,5.49535689e-02],[1.30768776e+00,-5.73566510e-01,-5.30483234e-01,1.48011758e+00,-1.18456427e+00,1.55804181e-01,-9.37420587e-01,-8.20714188e-01,1.08636761e+00,-1.25961267e+00],[2.00448406e+00,-7.28639999e-01,-9.23586099e-01,1.92799681e+00,-1.86857370e+00,3.15575347e-01,-1.41030148e+00,-1.15622841e+00,1.59374294e+00,-1.52000147e+00],[2.81283575e+00,-1.07753089e+00,-1.28693555e+00,1.64043476e+00,-2.68409201e+00,4.75062509e-01,-2.08103322e+00,-1.67334289e+00,2.37016486e+00,4.06457897e-02],[2.83473436e+00,-1.35484800e+00,-1.24993385e+00,1.48188523e+00,-2.65879239e+00,4.62660633e-01,-2.04587534e+00,-1.69349155e+00,2.46433899e+00,1.31991737e+00],[2.00228439e+00,-8.93130286e-01,-8.67381049e-01,9.86362796e-01,-1.92164535e+00,2.84090159e-01,-1.53042024e+00,-1.29226678e+00,1.76754166e+00,-2.54264858e-01],[3.30139397e+00,-1.93220672e+00,-1.48411958e+00,1.39849527e+00,-3.19542383e+00,4.30264914e-01,-2.37408493e+00,-2.16507198e+00,3.02694229e+00,4.78408233e-01],[3.78815204e+00,-1.76221634e+00,-1.75063277e+00,1.70981292e+00,-3.56567690e+00,5.81819070e-01,-2.75726526e+00,-2.31596731e+00,3.19560883e+00,7.40787070e-01],[4.57500372e-01,5.69964504e-01,-2.85745969e-01,-2.11278920e+00,-6.18482711e-01,1.04782611e-01,-3.45461906e-01,-6.15054791e-01,8.49833860e-01,-1.73337646e-01],[1.89453520e-01,2.11882230e-02,-3.96065483e-02,9.18108478e-02,-1.37360438e-01,1.02334735e-01,-4.86034968e-02,-4.00416070e-02,1.28840688e-02,-1.06160627e+00],[9.15915609e-02,-1.08835017e-03,-4.71209870e-02,1.97260679e+00,-3.18940438e-02,5.21235407e-02,-6.61836771e-02,3.29317982e-02,-4.32641795e-02,-5.98535812e+00],[5.37988658e-02,-2.89676731e-01,-1.74676614e-01,-2.03026151e-01,-4.16865107e-01,-9.30557923e-02,-1.34206047e-01,-3.35224750e-01,4.42082847e-01,1.52642675e-01],[2.92677922e-01,-2.16980995e-01,-1.24982254e-01,1.65432181e-01,-3.19708221e-01,3.78332328e-02,-2.27319461e-01,-3.00209552e-01,3.45437471e-01,-2.72710318e-01],[2.64780962e-01,-1.20498127e-01,-1.51850136e-01,-6.88391773e-02,-2.10870708e-01,3.67670958e-02,-1.79883426e-01,-1.63747626e-01,2.96386055e-01,2.00807523e-01],[3.00262373e+00,-1.23322360e+00,-1.42132462e+00,1.94518709e+00,-2.84517117e+00,4.71446737e-01,-2.10550888e+00,-1.84850494e+00,2.47033288e+00,-2.38902879e+00],[4.01689896e+00,-1.63125660e+00,-1.75151696e+00,2.03629755e+00,-3.67597365e+00,6.43724416e-01,-2.86071320e+00,-2.27657436e+00,3.21129841e+00,9.16386818e-01],[3.95006047e+00,-1.84863813e+00,-1.85280741e+00,2.33260221e+00,-3.80642159e+00,5.70420216e-01,-2.78514789e+00,-2.41712919e+00,3.33545441e+00,8.91128774e-01],[6.59762935e-01,-2.82540280e-01,-3.90336676e-01,3.27132976e-01,-6.73901955e-01,1.96305511e-01,-5.81900520e-01,-3.85105497e-01,5.64089987e-01,9.54024197e-01],[4.45179104e+00,-1.73022505e+00,-2.00398831e+00,1.06102332e+00,-4.27569625e+00,7.86063354e-01,-3.32564534e+00,-2.63810772e+00,3.51841117e+00,-1.87302446e+00],[7.08104917e+00,-2.54478425e+00,-3.18560464e+00,2.69465099e+00,-6.69269341e+00,1.13837190e+00,-5.15850563e+00,-4.05402150e+00,5.55546947e+00,7.31116370e-01],[3.02145073e-01,-3.76669876e-02,-7.14462192e-02,1.44002787e-01,-2.83213129e-01,-2.69610386e-02,-1.70428849e-01,-1.52792826e-01,2.44623879e-01,5.17832884e-01],[5.97333278e-01,-1.87917329e-01,-2.66714520e-01,-1.71578012e-01,-5.83771393e-01,6.42392254e-02,-4.51828398e-01,-3.26142694e-01,4.18349790e-01,9.30584633e-01],[6.05329093e-01,-2.88435324e-01,-2.32230003e-01,2.12629411e-01,-6.25370880e-01,1.28295502e-01,-4.76190991e-01,-4.31283887e-01,5.62797309e-01,9.23783050e-01],[5.91890760e+00,-2.70734875e+00,-2.60434032e+00,2.21460568e+00,-5.48688170e+00,9.78229997e-01,-4.25363694e+00,-3.41782694e+00,4.74679622e+00,2.53929791e+00],[9.19875526e-01,-4.68937781e-01,-3.87879346e-01,8.10791925e-01,-9.02322161e-01,7.17468156e-02,-7.09631177e-01,-6.08947286e-01,7.37900484e-01,-5.68006082e-02],[2.01448104e+00,-9.34743825e-01,-8.42750433e-01,1.29809705e+00,-1.93912924e+00,2.50835326e-01,-1.47571022e+00,-1.20487892e+00,1.57911095e+00,-1.56896487e+00],[7.04111458e-01,-4.93242659e-01,-3.35817721e-01,9.50683553e-01,-6.98558602e-01,1.40990478e-02,-4.29840200e-01,-4.45504525e-01,7.21403746e-01,-1.24971078e+00],[3.90095814e+00,-1.43767136e+00,-1.79304847e+00,3.75238469e+00,-3.60109956e+00,6.27409140e-01,-2.88826630e+00,-2.26687397e+00,3.08846638e+00,-4.99502044e-01],[4.12552249e-01,-2.52563594e-01,-2.65293993e-01,3.11898579e-01,-4.14426042e-01,8.73821739e-02,-2.75648375e-01,-3.42389492e-01,5.08207808e-01,-2.80952939e-01],[9.06141673e-01,-6.85486728e-01,-3.91335400e-01,4.86406924e-01,-8.30293234e-01,1.55816903e-01,-6.19212962e-01,-5.32859192e-01,7.52040654e-01,7.54103758e-01],[1.92608683e+00,-1.26805073e+00,-8.89889497e-01,5.78250897e-01,-1.74364659e+00,3.09079898e-01,-1.38052950e+00,-1.12199028e+00,1.56465982e+00,8.44667873e-01],[1.46239720e-01,-4.79900710e-02,-1.47544192e-01,4.29176921e-01,-1.69019035e-01,-1.39960997e-03,-1.41457737e-01,-1.37020672e-01,2.21660808e-01,-6.35215057e-01],[2.05960710e+00,-5.11261345e-01,-9.90459274e-01,-4.06664074e+00,-2.22256576e+00,3.97091027e-01,-1.60072281e+00,-1.48900045e+00,1.98788585e+00,1.21778154e+00],[3.73297531e+00,-2.55121283e+00,-1.68531217e+00,4.75100632e-01,-3.47807310e+00,5.93573830e-01,-2.71234020e+00,-2.15899735e+00,3.09890117e+00,1.70276708e+00],[8.25794570e-01,-3.99432075e-01,-4.57845321e-01,3.33229307e-01,-7.43532468e-01,1.59708612e-01,-5.80517117e-01,-4.82349271e-01,7.38681238e-01,-9.62850522e-01],[3.50825648e+00,-3.02159497e+00,-1.66135757e+00,1.94198278e+00,-3.52127244e+00,5.07071093e-01,-2.59585610e+00,-2.35938619e+00,3.20270741e+00,1.65694681e+00],[-1.65575223e-01,-2.82802508e-02,1.39961564e-01,-9.48663469e-01,1.04148676e-01,4.30141048e-02,1.19627193e-01,7.11929223e-02,-9.59004970e-02,3.25663809e-01],[2.96652390e-01,-1.35293793e-01,-1.80744654e-01,2.84173026e-01,-2.70103797e-01,-9.54254422e-03,-1.64207857e-01,-1.44596430e-01,2.97726813e-01,2.75374793e-01],[3.28803151e-01,-3.01013683e-01,-1.91933291e-01,4.02463519e-01,-3.86628329e-01,4.96937494e-02,-2.13666570e-01,-2.33471947e-01,3.90299088e-01,-1.32918011e+00],[2.68494400e+00,-1.84812415e+00,-1.15472836e+00,1.36450592e+00,-2.59235853e+00,1.93233793e-01,-1.71398234e+00,-1.70004114e+00,2.51416113e+00,-2.03004035e+00],[2.52770146e+00,-1.86029023e+00,-1.22071942e+00,7.11477549e-01,-2.48789943e+00,3.64293467e-01,-1.75281605e+00,-1.59018047e+00,2.30777933e+00,1.01278325e-01],[2.26363449e+00,-1.21910245e+00,-1.06735140e+00,6.41341654e-01,-2.10790306e+00,3.62135531e-01,-1.67063828e+00,-1.29978054e+00,1.88893241e+00,-7.87181289e-01],[1.95313608e+00,-9.31261866e-01,-8.99683238e-01,-4.30724906e+00,-1.73053687e+00,2.56319858e-01,-1.32883701e+00,-1.06228103e+00,1.55184258e+00,5.69072203e+00],[1.75109279e+00,-9.12095941e-01,-6.93039967e-01,4.42214149e-01,-1.51840301e+00,2.65588692e-01,-1.24176211e+00,-1.03961744e+00,1.41092687e+00,-4.12426565e-01],[9.37870937e-01,-3.19649022e-01,-3.22393409e-01,9.22988815e-01,-8.64273716e-01,1.37911414e-01,-6.59303955e-01,-4.29577972e-01,6.80531733e-01,-2.46247287e-01],[1.89875329e+00,-7.95696557e-01,-9.01611268e-01,2.07018611e+00,-1.82833956e+00,3.25723701e-01,-1.36863612e+00,-1.02453650e+00,1.59341526e+00,-5.44305296e-01],[7.16301420e-01,-2.37272311e-01,-3.05244646e-01,1.09990401e+00,-6.68914207e-01,1.28664396e-01,-5.57875466e-01,-3.40341791e-01,4.92152795e-01,7.06462533e-01],[9.04355718e-01,-2.98241415e-01,-4.40171912e-01,5.93973879e-01,-9.35573836e-01,1.28949406e-01,-6.30377361e-01,-5.24387389e-01,7.10039502e-01,1.83254003e-01],[1.41688315e+00,-6.09315387e-01,-6.86177138e-01,3.67806377e-01,-1.29332950e+00,2.74383622e-01,-1.06026361e+00,-7.84737545e-01,1.14954669e+00,1.65225829e+00],[1.82754351e+00,-9.77105131e-01,-8.51370328e-01,1.41726765e+00,-1.78348849e+00,3.34790989e-01,-1.30571380e+00,-1.17598690e+00,1.61273639e+00,1.66482413e+00],[4.83737732e+00,-2.72999015e+00,-2.16836433e+00,2.27914358e+00,-4.65350169e+00,7.50538494e-01,-3.46844302e+00,-2.94296948e+00,3.94765555e+00,6.23335218e-01],[-2.06796868e+00,1.64136771e+00,9.45883873e-01,-5.45262380e+00,1.99775352e+00,-3.04304304e-01,1.44976555e+00,1.26181128e+00,-1.82359485e+00,1.10545654e+01],[1.48373461e+00,-5.40158897e-01,-6.10457935e-01,1.35763456e-02,-1.30296753e+00,2.45954551e-01,-1.09236732e+00,-8.68440718e-01,1.08389132e+00,5.81573940e-01],[-9.04802443e-01,9.97506129e-01,4.04368817e-01,-2.39021751e+00,8.37999704e-01,-1.44058441e-01,8.74177596e-01,3.80914515e-01,-3.32486583e-01,3.48909625e+00],[2.18661661e+00,5.05045485e-02,-8.52328664e-01,-1.36118915e+00,-1.93190127e+00,4.16272763e-01,-1.54873757e+00,-1.09706469e+00,1.56306079e+00,5.61766308e-01],[6.86309975e+00,-3.35579650e+00,-3.09925042e+00,3.70375021e+00,-6.52888097e+00,1.13063738e+00,-4.92060296e+00,-4.07670256e+00,5.70506911e+00,-9.46569256e-01],[-7.37105083e+00,3.76537877e+00,3.30960233e+00,-2.05330876e+00,6.83223783e+00,-1.09040367e+00,5.21200809e+00,4.29984347e+00,-5.67308813e+00,-5.00618447e-01],[4.93736269e-01,-1.96899271e-01,-2.94394488e-01,2.31129320e-01,-4.93115941e-01,6.52763893e-02,-3.80015138e-01,-3.00450072e-01,4.04728938e-01,1.19340125e-01],[1.49423830e-01,5.88084871e-02,-4.47711210e-02,1.88795686e-01,-9.39876836e-02,1.07698873e-01,-7.37496400e-02,8.44124714e-03,8.27962243e-02,9.82377099e-01],[1.84228656e+00,-1.00605221e+00,-8.98095509e-01,8.29199600e-01,-1.95514086e+00,2.50402553e-01,-1.34153766e+00,-1.32376696e+00,1.80088374e+00,6.87753306e-01],[2.89805013e-01,-4.14097925e-02,-1.83254227e-01,1.59324980e-01,-1.90998129e-01,6.92706956e-02,-1.79196675e-01,-1.04326605e-01,2.74147985e-01,3.02761349e-01],[2.60110319e+00,-1.29298586e+00,-1.19282229e+00,2.04335548e+00,-2.45422093e+00,3.83282434e-01,-1.81480027e+00,-1.50726451e+00,2.21593797e+00,2.40420727e+00],[7.10840614e+00,-3.70585115e+00,-3.28186978e+00,6.82866640e+00,-6.81477192e+00,9.63159960e-01,-5.07653838e+00,-4.42154632e+00,5.98671565e+00,-2.99440797e+00],[5.29264643e+00,-4.79537433e+00,-2.57822888e+00,3.75788358e+00,-5.31579852e+00,7.00800316e-01,-3.68808427e+00,-3.65061662e+00,5.07897592e+00,9.86550124e-01],[5.32962282e+00,-5.81062814e+00,-2.34193075e+00,3.09307087e+00,-4.97547760e+00,8.79739886e-01,-3.68771689e+00,-3.15837556e+00,4.26386426e+00,-1.91809710e+00],[2.06341525e-01,-7.11781733e-02,-4.47106346e-02,2.19857463e-01,-2.45628711e-01,7.26807411e-02,-7.54090197e-02,-4.61386705e-02,8.12919051e-02,-1.14191951e+00],[1.22774626e+00,-5.02774203e-01,-6.38991443e-01,1.29520703e+00,-1.23162611e+00,2.80944255e-01,-9.42934372e-01,-7.84056867e-01,1.04139395e+00,5.54290502e-01],[1.10058693e+00,-2.22269209e+00,-6.41399101e-01,4.98392873e+00,-1.23027765e+00,1.56676259e-01,-8.45550770e-01,-1.01218332e+00,1.18823773e+00,-4.66677126e-01],[4.65342511e-01,-1.76548685e-01,-1.65898284e-01,1.16973477e-01,-5.21644265e-01,1.32477636e-01,-3.32135089e-01,-3.36623788e-01,3.78529037e-01,4.82147702e-01],[2.49746743e+00,-1.11113304e+00,-1.15499932e+00,1.72802397e+00,-2.30638200e+00,3.87087247e-01,-1.72584176e+00,-1.50650034e+00,2.05865657e+00,6.91230418e-01],[3.31181127e+00,-1.63519347e+00,-1.42094410e+00,1.47796972e+00,-3.16917240e+00,4.84983611e-01,-2.42950743e+00,-2.05967793e+00,2.75271968e+00,3.14694762e-01],[6.11901233e+00,-2.51269670e+00,-2.75202568e+00,3.47751215e+00,-5.70910628e+00,9.62859259e-01,-4.34983380e+00,-3.58689889e+00,4.95597215e+00,1.78315720e-01],[3.93863567e+00,-9.92438989e-01,-1.65523188e+00,-4.64031896e-01,-3.63930201e+00,5.74835114e-01,-2.79552755e+00,-2.26099064e+00,3.27500050e+00,6.83155035e+00],[2.05168565e+00,-1.31792281e+00,-9.52602413e-01,1.33388078e+00,-1.88424683e+00,2.85423851e-01,-1.38717425e+00,-1.24380741e+00,1.74630735e+00,-1.01164083e+00],[1.31466763e+00,-7.55362452e-01,-5.93030005e-01,7.75018522e-01,-1.36691502e+00,1.84732116e-01,-9.71553939e-01,-7.86937010e-01,1.13965107e+00,-4.51039218e-01],[-1.80873837e+00,1.52170903e+00,9.38867131e-01,-7.68039185e+00,1.80450140e+00,-2.55585000e-01,1.23079712e+00,1.09048980e+00,-1.46630579e+00,1.63103590e+01],[2.03819644e+00,-1.07464711e+00,-9.33312650e-01,8.16332493e-01,-2.13008286e+00,2.72634520e-01,-1.54811547e+00,-1.46973178e+00,1.94869084e+00,9.00352379e-01],[9.37778036e-01,-7.77658280e-01,-4.60258699e-01,8.04570854e-01,-9.71566359e-01,-4.27729814e-02,-5.42173884e-01,-7.62578114e-01,9.97453428e-01,-1.02140695e+00],[6.09069160e-01,-2.68442784e-01,-3.55098699e-01,-2.31801778e-01,-6.23535644e-01,1.56535321e-01,-4.15556703e-01,-4.28948931e-01,4.99330237e-01,7.29745260e-02],[9.83830758e-01,-3.87108765e-01,-3.93318038e-01,4.63584872e-01,-8.20183959e-01,1.43599310e-01,-6.69117818e-01,-5.48944918e-01,7.86858038e-01,-3.25302591e-01],[6.62534894e-02,1.66935768e+00,-1.52164067e-01,-8.53615757e-01,-3.88112312e-01,5.11563843e-01,-8.60634033e-02,-9.15344539e-02,3.60644337e-01,-3.73950660e-02],[-5.99517776e-02,3.31175296e+00,-4.14559721e-03,-8.04894261e-01,5.06038098e-02,8.52154030e-01,-7.77624148e-02,3.28596834e-01,-1.89377193e-01,-6.21373014e-01],[2.37630574e+00,-1.40335852e+00,-1.14580733e+00,1.36367199e+00,-2.27185437e+00,1.72913751e-01,-1.50223670e+00,-1.52006872e+00,2.36822917e+00,3.22786711e-02],[2.81883734e+00,-1.22537888e+00,-1.29226364e+00,2.73535983e+00,-2.64598461e+00,4.04778944e-01,-1.91166247e+00,-1.73769363e+00,2.42822342e+00,-5.74547246e-02],[4.56312400e-01,-7.55361672e-01,-2.62307028e-01,7.81513442e-01,-6.04396338e-01,9.55824591e-02,-3.78396744e-01,-3.44407424e-01,4.67717708e-01,-1.12363086e+00],[-6.57890288e-01,2.58199151e-01,3.03339725e-01,3.17673201e+00,6.93868827e-01,-1.54048339e-01,5.01321160e-01,3.77318917e-01,-5.38626819e-01,1.05335746e+00],[-5.27904039e+00,1.42456266e+00,2.20065872e+00,-1.12122156e+01,4.61637683e+00,-6.97257005e-01,3.67992943e+00,2.69874256e+00,-3.58876014e+00,1.35779190e+00],[-7.26348561e+00,-7.01800419e-01,2.87435911e+00,-3.59720410e-01,6.46746720e+00,-1.69754518e+00,5.30114739e+00,3.42305684e+00,-4.59661278e+00,1.47761109e-01],[1.26066760e+00,-8.36875988e-01,-6.00517920e-01,-4.61392624e-02,-1.12557086e+00,2.60134127e-01,-9.26426946e-01,-7.19217802e-01,1.02526600e+00,1.23728624e-01],[5.81950570e+00,-2.48641694e+00,-2.68224714e+00,7.29904877e+00,-5.48020833e+00,9.17665957e-01,-4.26569218e+00,-3.50308090e+00,4.87882240e+00,-5.84383523e+00],[-1.00531120e+01,3.17722511e+00,4.39465788e+00,9.60852153e-01,9.32370346e+00,-2.10674685e+00,7.69593573e+00,5.29318783e+00,-6.95726494e+00,1.09924996e+00],[4.40399389e+00,-2.54171443e+00,-2.39498229e+00,1.36990242e+00,-4.85586338e+00,6.73408441e-01,-3.54319053e+00,-3.50596402e+00,5.09710258e+00,-1.30760372e+00],[1.86578141e+00,-4.52568481e-01,-8.59801163e-01,-1.72487328e+00,-1.79563051e+00,3.99651747e-01,-1.42656419e+00,-1.12011701e+00,1.58042161e+00,6.67306246e-01],[1.71321495e+00,-7.53457842e-01,-8.34350816e-01,5.51283478e-01,-1.64279002e+00,3.10787606e-01,-1.16238842e+00,-9.67227035e-01,1.41526494e+00,-1.87526741e+00],[-9.63927018e-02,5.39229146e-02,3.71780081e-02,-2.94024919e-01,-2.16732266e-02,1.52412705e-02,5.28620048e-02,2.39886853e-02,-7.12848449e-02,9.37446115e-01],[6.24482169e-01,-6.45040290e-01,-2.76227554e-01,2.14741018e-01,-7.07440003e-01,1.41726965e-01,-4.65774310e-01,-3.93012118e-01,5.76103897e-01,9.05767416e-01],[2.78485286e+00,-1.75658681e+00,-1.22834871e+00,6.14849041e-01,-2.75392701e+00,2.99853326e-01,-1.93489787e+00,-1.85985669e+00,2.58985423e+00,-2.27760115e+00],[3.04897662e+00,-1.25400498e+00,-1.31290096e+00,1.87097673e+00,-2.83456945e+00,4.72573333e-01,-2.14901486e+00,-1.80715242e+00,2.44865897e+00,4.33171504e-01],[4.66284064e+00,-1.10059859e+00,-1.90213197e+00,7.33749871e+00,-4.15489804e+00,6.70943882e-01,-3.19009735e+00,-2.48816333e+00,3.60192459e+00,-9.82238555e+00],[1.57069047e+00,-1.05978126e+00,-7.55663877e-01,1.31417134e+00,-1.58717597e+00,2.28738144e-01,-1.05832848e+00,-1.14330316e+00,1.48588378e+00,3.29877267e-01],[4.61547094e+00,-2.14451237e+00,-2.13373156e+00,1.46030654e+00,-4.36523162e+00,6.79894066e-01,-3.35733489e+00,-2.80390716e+00,3.76934726e+00,-4.51510471e-01],[1.53322616e+00,-7.94707602e-01,-6.74459337e-01,1.03311831e+00,-1.41377692e+00,2.94624934e-01,-1.07898595e+00,-9.82444016e-01,1.28300689e+00,3.25530665e-01],[1.41293699e+00,-5.61268465e-01,-6.14623194e-01,1.11380799e+00,-1.22898312e+00,2.84469269e-01,-9.46611298e-01,-7.75866969e-01,1.08130605e+00,-8.21601688e-01],[1.07437025e+00,-4.60390648e-01,-4.09563179e-01,1.41793100e+00,-9.27700196e-01,1.15494750e-01,-7.27340804e-01,-5.54400814e-01,8.70401496e-01,-3.11154374e-01],[8.49675844e-01,-3.50597349e-01,-3.71036240e-01,9.22929019e-01,-6.81964664e-01,1.92571962e-01,-6.26645357e-01,-4.69568481e-01,5.77704948e-01,-1.41531208e-01],[2.18765250e+00,-1.50592755e+00,-9.77158422e-01,5.56158945e-01,-2.02099741e+00,3.31282303e-01,-1.53577655e+00,-1.28476033e+00,1.80179687e+00,-1.77933459e+00],[1.81358320e+00,-8.47837396e-01,-7.60225858e-01,8.43918874e-01,-1.70640879e+00,2.33092150e-01,-1.30934004e+00,-1.07066908e+00,1.46831726e+00,-1.21850001e+00],[3.25410145e-01,-4.58190893e-01,-1.26327016e-01,-2.14637743e+00,-3.20078167e-01,-2.40915899e-02,-2.39816457e-01,-2.77043539e-01,3.36127903e-01,6.15685533e+00],[2.76327390e+00,-1.61076807e+00,-1.21094086e+00,2.32089641e+00,-2.61309298e+00,3.75713010e-01,-1.96550377e+00,-1.64058185e+00,2.38073564e+00,-1.48821598e+00],[1.34073421e+00,-5.97939001e-01,-6.50806043e-01,-1.28925150e-01,-1.20931953e+00,2.10654243e-01,-1.02696587e+00,-8.45666079e-01,1.16348439e+00,1.45022767e-01],[3.37253339e+00,-1.74399492e+00,-1.58116014e+00,2.08914472e+00,-3.29676400e+00,3.95340801e-01,-2.28907538e+00,-2.20789507e+00,3.09296238e+00,-7.60431975e-01],[4.87936670e+00,-1.89803163e+00,-2.15151536e+00,2.44179818e+00,-4.51798288e+00,7.94926458e-01,-3.50355062e+00,-2.84389176e+00,3.92626917e+00,6.91565107e-01],[1.13594658e+00,-8.52226164e-01,-4.86312424e-01,7.53184174e-01,-1.00188384e+00,1.47163515e-01,-7.09278246e-01,-6.65203666e-01,1.07127108e+00,3.92128407e-02],[8.02939688e-01,-2.55666033e-01,-4.09287825e-01,8.87829267e-02,-7.65129461e-01,1.70708423e-01,-6.09000950e-01,-3.71263598e-01,5.98476490e-01,1.50857873e+00],[2.20161585e+00,-1.07492518e+00,-9.51150144e-01,1.41301898e+00,-2.10563872e+00,3.20561506e-01,-1.57500398e+00,-1.37510712e+00,1.85504875e+00,-4.09224957e-01],[1.08263671e+01,-4.45939998e+00,-4.80602319e+00,5.44803838e+00,-1.01596570e+01,1.67193902e+00,-7.86246708e+00,-6.31146926e+00,8.76985552e+00,-5.98998826e-01],[2.12574609e+00,-1.66621706e+00,-9.33213616e-01,2.89710730e+00,-1.95740662e+00,1.61580705e-01,-1.31181784e+00,-1.38737250e+00,1.91170789e+00,-2.15949176e+00],[1.62884668e+00,-2.35936561e+00,-9.26805871e-01,3.02682213e+00,-1.61294970e+00,2.13583922e-01,-1.24202016e+00,-1.23472548e+00,1.58013726e+00,-3.19448350e-01],[-8.70577318e-01,8.55825838e-01,3.99327777e-01,-1.10038727e+00,8.26186258e-01,2.97906203e-02,5.60006734e-01,6.05664094e-01,-7.20841599e-01,1.60743441e+00],[1.81038003e+00,-3.55991603e-01,-8.84559257e-01,-1.41853485e+00,-1.99550028e+00,3.02387447e-01,-1.24338930e+00,-1.34897491e+00,1.95646551e+00,-4.02126208e+00],[1.48982965e+00,-6.76367875e-01,-5.95391289e-01,6.63193812e-01,-1.34087593e+00,2.94759998e-01,-1.02014925e+00,-8.31477712e-01,1.14820413e+00,7.98757095e-02],[1.41893560e+00,-6.15936108e-01,-7.05906686e-01,2.77017557e-01,-1.42163663e+00,2.20673438e-01,-1.14072084e+00,-8.79715443e-01,1.22844739e+00,6.68564074e-01],[1.53862965e+00,-7.67681951e-01,-6.47191102e-01,6.60554946e-01,-1.51100893e+00,2.12641535e-01,-1.10931910e+00,-9.82790115e-01,1.27580520e+00,1.53397973e-01],[4.01067526e+00,-2.21320877e+00,-1.78513961e+00,1.64441983e+00,-3.70350040e+00,5.36940057e-01,-2.84820136e+00,-2.37065338e+00,3.23153976e+00,1.29422282e+00],[1.01117250e-01,-1.35707438e-01,-2.40068038e-02,1.40971825e-01,-1.20291285e-01,5.65121998e-03,9.16990001e-03,-9.24672665e-02,5.68701039e-02,-5.01262554e-03],[2.34031699e+00,-2.13261524e+00,-1.10818383e+00,3.42249270e+00,-2.32507460e+00,1.59256540e-01,-1.53355107e+00,-1.54251811e+00,2.21076618e+00,-1.95072159e+00],[2.14060902e+00,-1.99211120e+00,-9.54723894e-01,4.63354931e+00,-2.04896447e+00,1.77695491e-01,-1.31573554e+00,-1.40587890e+00,1.90917806e+00,-6.51980625e+00],[9.67937789e-01,-6.13481707e-01,-4.34154951e-01,1.11798759e+00,-9.45799636e-01,9.85153915e-02,-6.74303580e-01,-6.38805049e-01,7.61340107e-01,-9.36356299e-01],[1.46129900e+00,-5.55671041e-01,-6.06171894e-01,9.28920167e-01,-1.42647726e+00,1.81577452e-01,-1.09395299e+00,-8.68027747e-01,1.14250156e+00,-7.90656748e-01],[-2.76330158e-02,9.03205181e-02,-8.48987771e-03,-1.69263616e-01,9.87739275e-02,-3.91208135e-02,4.41242967e-02,9.62427849e-02,-1.45013921e-01,7.17795228e-01],[1.27666226e+00,-7.82454720e-01,-5.52554110e-01,1.17003749e+00,-1.33192044e+00,5.96920992e-02,-8.56590943e-01,-8.97945050e-01,1.19337403e+00,-1.14245358e+00],[5.10161058e+00,-2.25646912e+00,-2.28939252e+00,3.45944773e+00,-4.87100096e+00,8.77259870e-01,-3.76434396e+00,-3.00158355e+00,4.08136511e+00,-3.88304756e-01],[-1.12176115e+01,3.07019954e+00,4.61633634e+00,-1.74387133e+00,9.95393633e+00,-2.74443104e+00,7.84552345e+00,5.64346981e+00,-7.42552963e+00,-1.09387431e+00],[6.99373852e-01,-3.12634072e-01,-3.32044513e-01,1.28654705e+00,-7.53181703e-01,8.21249307e-02,-4.98860554e-01,-4.12094724e-01,5.64726600e-01,-2.56976710e+00],[4.57099212e-01,-3.24516588e-01,-1.84157690e-01,1.85366031e+00,-4.17881989e-01,1.37174054e-02,-2.34292695e-01,-2.92000716e-01,4.34420251e-01,2.75404073e+00],[2.68457275e+00,-1.13017953e+00,-1.17842277e+00,-2.85202365e-01,-2.54963260e+00,3.09064183e-01,-1.83640241e+00,-1.72851527e+00,2.40229903e+00,-2.89023219e+00],[3.99158961e+00,-1.72114979e+00,-1.75026913e+00,1.99524342e+00,-3.77665006e+00,6.27807645e-01,-2.82303761e+00,-2.28308667e+00,3.27394161e+00,1.27636861e+00],[1.07766304e+00,-7.09835341e-01,-5.14654751e-01,9.27261819e-01,-9.27788684e-01,2.09817920e-01,-7.94048418e-01,-5.79138726e-01,7.45831111e-01,1.18854381e+00],[-2.74296248e+00,-1.81539288e-01,1.34618051e+00,-4.10042550e-01,2.75975070e+00,-7.49214171e-01,2.06287770e+00,1.55966445e+00,-2.10931124e+00,-1.11397436e+00],[1.38094298e+00,-1.85993005e+00,-5.98121343e-01,-2.88779600e-01,-1.22799066e+00,9.45866915e-02,-1.02473462e+00,-7.73486666e-01,1.09554918e+00,3.22775374e-01],[3.87714534e+00,-1.75980130e+00,-1.77147709e+00,3.21351401e+00,-3.78283246e+00,5.46101643e-01,-2.80904925e+00,-2.34043953e+00,3.29821324e+00,-2.36006525e+00],[2.11361581e+00,-1.07826191e+00,-9.13190326e-01,7.07152387e-01,-1.96809053e+00,2.83331251e-01,-1.57658761e+00,-1.23983450e+00,1.66972530e+00,-2.32529877e-01],[2.38570459e+00,-8.71140030e-01,-1.05617726e+00,3.92297785e-01,-2.19716576e+00,3.71552590e-01,-1.67855277e+00,-1.33784907e+00,1.83903347e+00,4.31635807e-01],[8.64100106e+00,-3.33440572e+00,-3.93206616e+00,3.45419107e+00,-8.17805223e+00,1.44842712e+00,-6.39617192e+00,-5.06552825e+00,7.01879945e+00,-1.65124573e+00],[1.07512343e+01,-4.27533595e+00,-4.70539419e+00,5.76598163e+00,-9.85382291e+00,1.66115551e+00,-7.68377296e+00,-6.23025292e+00,8.61702591e+00,-1.85385606e+00],[6.10797370e+00,-2.78850870e+00,-2.72541549e+00,3.78971592e+00,-5.65285477e+00,9.02915950e-01,-4.32818996e+00,-3.67697313e+00,5.01421183e+00,1.05017716e-02],[4.20309524e-01,-6.10234739e-01,-1.37748637e-01,-2.53024983e-01,-3.33856204e-01,-2.44695672e-02,-3.14072981e-01,-2.77707579e-01,2.63110498e-01,-8.42791666e-01],[4.96121383e+00,-4.49289140e+00,-2.55644810e+00,2.60712608e+00,-5.42614376e+00,2.92371618e-01,-3.45081279e+00,-3.81536539e+00,5.44126592e+00,-1.18869972e-01],[1.33584605e+00,-6.70889953e-01,-6.51748618e-01,4.32881947e-01,-1.26987278e+00,1.89847586e-01,-9.11827531e-01,-7.26388535e-01,1.16169289e+00,3.84137906e-01],[-8.67993647e-02,-4.17272458e-01,3.17465610e-02,-1.95980145e+00,9.94957018e-02,-5.97576433e-02,8.14781467e-02,-6.38448661e-03,1.03137206e-02,2.88243951e+00],[-4.82393080e+00,4.34580862e-01,1.83778270e+00,1.34828462e+00,4.05035726e+00,-9.11488668e-01,3.41943600e+00,2.15164830e+00,-2.77247639e+00,-2.49207211e+00],[1.59044272e+00,-6.36308355e-01,-6.54958779e-01,7.74090978e-01,-1.57058594e+00,3.07549781e-01,-1.17139958e+00,-8.96540895e-01,1.34478441e+00,6.00693997e-01],[2.36447987e-01,-3.72188294e-03,-5.62334114e-02,3.83035132e-01,-1.48062572e-01,8.92448534e-02,-1.03269021e-01,-1.26768731e-01,7.98588226e-02,-9.91745699e-01],[4.02574936e+00,-1.80460004e+00,-1.74062687e+00,2.19114385e+00,-3.70775407e+00,5.41681030e-01,-2.84770141e+00,-2.34210967e+00,3.28935083e+00,-8.97332259e-01],[3.79711776e+00,-1.51120929e+00,-1.63507554e+00,1.94512072e+00,-3.54665258e+00,6.17146030e-01,-2.69548099e+00,-2.18029027e+00,3.04990828e+00,1.99024285e-01],[2.61314250e+00,-8.32178088e-01,-1.17441933e+00,8.86890874e-01,-2.46161032e+00,4.33061608e-01,-1.84045725e+00,-1.51027520e+00,2.06226183e+00,-5.04790034e-01],[1.91628566e+00,-1.18025378e+00,-8.29593456e-01,8.05589864e-01,-1.83531465e+00,2.33892404e-01,-1.33577685e+00,-1.22886598e+00,1.63724059e+00,-4.10720011e-01],[6.62692963e+00,-2.59763094e+00,-2.91858978e+00,2.65029845e+00,-6.09864781e+00,1.11191040e+00,-4.76486241e+00,-3.77353929e+00,5.25968691e+00,2.36029951e+00],[7.08400174e-01,-2.73048546e-01,-2.36510947e-01,3.36250778e-01,-5.71174839e-01,1.32306595e-01,-4.45949679e-01,-3.83520526e-01,5.96793713e-01,3.54596706e-01],[1.23538410e+00,-2.10377052e+00,-7.42293960e-01,1.80936487e-01,-1.39298090e+00,1.21137143e-01,-9.67345410e-01,-9.97545904e-01,1.30398797e+00,2.93336429e+00],[1.10059929e+00,-4.29217652e-01,-4.62790655e-01,2.45630122e-01,-9.62932535e-01,2.00964451e-01,-7.95797397e-01,-5.97555098e-01,8.36931164e-01,5.84278745e+00],[1.41930829e-01,-1.41177740e-01,-9.59174836e-02,7.04293130e-01,-1.75886186e-01,-5.46187095e-03,-1.87232111e-01,-1.32830584e-01,1.12281381e-01,-5.18262082e-01],[5.05409005e+00,-2.75490475e+00,-2.28290437e+00,3.15739781e+00,-4.89829982e+00,7.46847837e-01,-3.67608657e+00,-2.99246980e+00,4.21482671e+00,-1.55073598e+00],[5.04422898e+00,-2.57463285e+00,-2.23923299e+00,2.05060374e+00,-4.78020756e+00,7.59102141e-01,-3.62905266e+00,-3.05720559e+00,4.07705086e+00,-2.01981087e-01],[6.86730357e+00,-3.16899070e+00,-3.08451485e+00,3.82067152e+00,-6.36784429e+00,1.05174659e+00,-4.82698021e+00,-3.89678903e+00,5.45044777e+00,2.24503587e+00],[1.10115407e+00,-4.27582974e-01,-5.18979820e-01,4.61401314e-01,-1.10030676e+00,1.20737405e-01,-7.50049492e-01,-7.17535837e-01,8.95997306e-01,-5.54403230e-02],[6.49620958e+00,-2.46214842e+00,-2.89557351e+00,2.51012889e+00,-6.07274733e+00,1.15011924e+00,-4.82476404e+00,-3.71566394e+00,5.10878845e+00,-3.57464191e-01],[9.75475816e+00,-3.74675408e+00,-4.30301075e+00,3.90565921e+00,-8.90796502e+00,1.54992757e+00,-7.01391805e+00,-5.48830494e+00,7.69437229e+00,1.64968191e-02],[9.69119067e+00,-3.65917540e+00,-4.30657589e+00,2.93660450e+00,-9.00706646e+00,1.74133468e+00,-7.14684186e+00,-5.54299030e+00,7.55069660e+00,-3.31079842e-01],[1.12639916e+00,-5.56472102e-01,-4.79362727e-01,4.15575838e-01,-1.09868423e+00,1.66609536e-01,-7.85273124e-01,-5.94363459e-01,9.72816033e-01,8.12193113e-02],[5.81606315e+00,-2.67705593e+00,-2.58154533e+00,3.00329162e+00,-5.51227727e+00,9.61633335e-01,-4.24720249e+00,-3.34450900e+00,4.76294200e+00,3.67331153e+00],[5.95482543e+00,-2.31621075e+00,-2.63172792e+00,3.49256954e+00,-5.46642280e+00,9.08259836e-01,-4.34141788e+00,-3.43526303e+00,4.68380231e+00,-8.04171506e-01],[7.07909904e-01,-4.31734456e-01,-4.20609804e-01,5.15215206e-01,-8.07050650e-01,7.34622459e-02,-5.75576412e-01,-5.92614462e-01,7.03939606e-01,-4.01437293e-01],[8.81533296e-01,-5.38752340e-01,-4.24798120e-01,2.90287761e-01,-7.66556184e-01,4.24680917e-02,-5.71211434e-01,-5.28188633e-01,7.46700273e-01,-2.46539505e-01],[5.84835874e+00,-2.53962500e+00,-2.55676000e+00,2.40995142e+00,-5.39524651e+00,9.31631054e-01,-4.21370686e+00,-3.41601124e+00,4.67941286e+00,-2.88010541e-01],[1.11700812e+00,-5.39001086e-01,-4.64473352e-01,4.90822569e-01,-1.13752262e+00,1.61342400e-01,-7.98397635e-01,-7.59016170e-01,9.23320651e-01,-8.28079852e-03],[5.91339420e+00,-2.64462260e+00,-2.55032741e+00,1.99323691e+00,-5.46198264e+00,1.00179938e+00,-4.28931799e+00,-3.45424394e+00,4.75193982e+00,1.10171874e+00],[5.59056965e+00,-2.27604447e+00,-2.48958639e+00,1.92864645e+00,-5.05889312e+00,9.59695452e-01,-3.93901236e+00,-3.26505410e+00,4.43177955e+00,1.37378584e-01],[1.86148516e+00,-7.57134810e-01,-8.32773324e-01,1.08135539e+00,-1.81282612e+00,3.43088964e-01,-1.39568676e+00,-1.18481057e+00,1.54929703e+00,4.91997788e-02],[6.45649492e+00,-3.08731372e+00,-2.88226412e+00,2.94449074e+00,-6.02019517e+00,9.83435089e-01,-4.60093190e+00,-3.77781223e+00,5.27937215e+00,-1.20984571e-02],[4.72366530e+00,-2.53422051e+00,-2.02576224e+00,1.91482093e+00,-4.24545203e+00,7.31991200e-01,-3.41616688e+00,-2.63940590e+00,3.58718462e+00,3.27584222e-01],[7.90329595e+00,-3.04540854e+00,-3.50685848e+00,3.21896688e+00,-7.38532972e+00,1.41143783e+00,-5.82688829e+00,-4.55969600e+00,6.16928295e+00,-5.96351862e-01],[2.40056932e+00,-9.07679147e-01,-1.03231715e+00,1.04857612e+00,-2.25244653e+00,4.42094381e-01,-1.69685972e+00,-1.42067707e+00,1.85468815e+00,-1.05239161e+00],[1.72343844e+00,-7.31291654e-01,-7.58528997e-01,6.92862925e-01,-1.54232946e+00,2.68390985e-01,-1.22469360e+00,-1.03005745e+00,1.38994116e+00,-2.74547165e-01],[5.74797041e+00,-2.68278529e+00,-2.59789985e+00,2.71316273e+00,-5.40866108e+00,9.77877028e-01,-4.09763613e+00,-3.36993662e+00,4.68494743e+00,4.38847796e-01],[6.16670022e+00,-2.93048785e+00,-2.73299909e+00,3.69489983e+00,-5.87991731e+00,9.34486404e-01,-4.45749875e+00,-3.70813502e+00,5.10698283e+00,-1.79173141e+00],[7.09492671e+00,-3.51011857e+00,-3.08405869e+00,3.84846202e+00,-6.57136977e+00,1.05523762e+00,-5.05063681e+00,-4.10482080e+00,5.80622936e+00,-1.13512685e+00],[5.35474982e+00,-2.61646292e+00,-2.49604668e+00,3.23534883e+00,-5.32049626e+00,7.36952422e-01,-3.66022276e+00,-3.38309688e+00,4.57577000e+00,-1.68992093e+00],[4.44192542e+00,-2.18323954e+00,-1.91850551e+00,1.64930697e+00,-4.17286214e+00,7.10611783e-01,-3.16674752e+00,-2.63093614e+00,3.71208265e+00,2.35378892e-01],[4.28110952e+00,-1.89707773e+00,-1.93721281e+00,2.38362121e+00,-4.03679052e+00,6.61203807e-01,-3.01860726e+00,-2.48839299e+00,3.48325935e+00,-1.23611355e+00],[6.27434262e+00,-2.78659934e+00,-2.81545880e+00,2.62006558e+00,-5.84101912e+00,9.34791069e-01,-4.47207370e+00,-3.70291886e+00,5.18687572e+00,2.36572827e+00],[1.10224700e+00,-3.90406213e-01,-4.58480855e-01,3.55975917e-01,-1.03104762e+00,1.67378919e-01,-8.12428484e-01,-6.66111285e-01,7.83645696e-01,2.24460340e-01],[8.92887462e-01,-4.10005857e-01,-4.20539338e-01,3.93609026e-01,-7.26081218e-01,1.04031447e-01,-6.76002996e-01,-4.27505911e-01,7.15552920e-01,-1.18609974e-01],[4.20114092e+00,-1.95677631e+00,-1.97564150e+00,1.63616382e+00,-4.11250242e+00,5.79788210e-01,-3.09500298e+00,-2.56893356e+00,3.77158703e+00,-9.22549509e-01],[6.87142668e+00,-2.59659204e+00,-3.03277957e+00,2.77480011e+00,-6.31341511e+00,1.14412736e+00,-4.88624629e+00,-3.85663432e+00,5.43133058e+00,7.42451858e-01],[1.15692502e+00,-4.98119836e-01,-5.00808422e-01,5.57232827e-01,-1.12949736e+00,1.53410814e-01,-8.19119635e-01,-7.26301300e-01,9.76404856e-01,-4.45299676e-02],[3.48765622e+00,-1.45124445e+00,-1.50994593e+00,1.40096999e+00,-3.42491377e+00,5.94978897e-01,-2.56265216e+00,-2.15406991e+00,2.98576222e+00,-1.41570890e-01],[5.60679825e+00,-2.74837331e+00,-2.54263819e+00,3.95616524e+00,-5.21859964e+00,8.43213679e-01,-3.97365749e+00,-3.28858725e+00,4.58360702e+00,-4.06107945e+00],[5.68908114e+00,-2.77509810e+00,-2.53009409e+00,3.63159902e+00,-5.34548520e+00,9.22869243e-01,-4.10918077e+00,-3.33659232e+00,4.64015183e+00,-2.42577504e+00],[1.18089290e+00,-5.49673319e-01,-4.91462471e-01,6.52000567e-01,-1.03044591e+00,1.82335851e-01,-8.33615891e-01,-7.80848202e-01,1.02219308e+00,1.86899677e-01],[6.52571725e+00,-3.09900009e+00,-2.92212971e+00,2.55092131e+00,-6.11521803e+00,1.01879107e+00,-4.57615549e+00,-3.79028789e+00,5.23091176e+00,-2.96834460e+00],[1.98978311e+00,-1.51943490e+00,-8.93325337e-01,2.33046722e-01,-1.98483156e+00,2.69190696e-01,-1.47335767e+00,-1.28764166e+00,1.70753181e+00,2.61608451e+00],[-4.52273632e+00,3.31298029e-01,2.01273746e+00,-2.11298143e+00,4.42878469e+00,-8.37266815e-01,3.30229417e+00,2.49331995e+00,-3.48773489e+00,9.32295764e-01],[6.20877213e-01,-1.70862565e+00,-4.56585666e-01,6.15609147e+00,-6.82323768e-01,9.97284508e-02,-5.56580991e-01,-5.93819559e-01,7.66646693e-01,-8.75517859e+00],[9.44111085e-01,-3.81039017e-01,-3.77433098e-01,5.63743524e-01,-9.25882766e-01,1.95765422e-01,-7.81593854e-01,-6.46636300e-01,8.49445022e-01,-5.20191106e-01],[1.03719729e+00,-4.58807460e-01,-5.20163900e-01,3.23802966e-01,-1.02404769e+00,1.30195604e-01,-8.26494715e-01,-5.90824144e-01,8.77711320e-01,-1.64046597e-01],[7.02132712e-01,-2.27648695e-01,-3.27978759e-01,7.29672117e-01,-6.68166670e-01,1.78431797e-01,-4.02862277e-01,-3.48589775e-01,4.38716295e-01,-6.52442657e-01],[8.98114190e-01,-4.13576101e-01,-4.25925622e-01,2.66133544e-01,-8.82249130e-01,1.41547565e-01,-6.41494908e-01,-5.25679198e-01,8.12595331e-01,2.20255594e-01],[1.67849576e+00,-5.69276565e-01,-7.05055276e-01,7.11398498e-01,-1.45306342e+00,3.30741600e-01,-1.25691295e+00,-8.58389291e-01,1.20583851e+00,1.36659032e-01],[4.47135483e+00,-1.55831235e+00,-1.96175442e+00,1.28711051e+00,-4.09029916e+00,6.90368822e-01,-3.24207992e+00,-2.43644296e+00,3.51117517e+00,5.30314565e-01],[6.51338327e+00,-2.68272422e+00,-2.82399647e+00,1.69931512e+00,-6.09174701e+00,1.00219477e+00,-4.60305067e+00,-3.83035122e+00,5.34141449e+00,-8.41646127e-01],[8.62132297e-01,-3.30086086e-01,-4.39597308e-01,3.05891148e-01,-8.54820265e-01,1.79558804e-01,-7.24400232e-01,-4.89618087e-01,7.25821040e-01,1.27162112e-01],[1.57150398e+00,-6.45206707e-01,-7.00430994e-01,7.71301326e-01,-1.43548199e+00,2.26731656e-01,-1.05687663e+00,-8.44700760e-01,1.26703407e+00,-2.71061222e-01],[1.96892075e+00,-8.89762382e-01,-9.55643169e-01,9.40437754e-01,-1.90462076e+00,3.48371628e-01,-1.42583904e+00,-1.20799969e+00,1.60631155e+00,-1.00255394e-01],[6.35197480e+00,-2.91915352e+00,-2.90646301e+00,2.10032152e+00,-5.96863738e+00,1.04297897e+00,-4.54102940e+00,-3.76593927e+00,5.09004302e+00,1.11439475e+00],[6.04145329e-01,-4.08310398e-01,-2.74529359e-01,3.04869190e-01,-6.56883596e-01,5.92431242e-02,-4.62038658e-01,-3.66486789e-01,6.36747206e-01,1.10485214e-01],[-1.28909318e+00,-2.66181062e+00,5.04033039e-01,-2.36397628e-01,1.22724919e+00,-1.53868522e-01,1.02191513e+00,6.36932115e-01,-1.03087602e+00,1.70066061e+00],[1.48610576e+00,-5.74024361e-01,-6.43402022e-01,5.85337104e-01,-1.48188597e+00,3.13118087e-01,-1.12958900e+00,-8.72615955e-01,1.28646110e+00,3.30208888e-01],[7.20785144e+00,-2.97636859e+00,-3.17036467e+00,3.19518765e+00,-6.76791314e+00,1.26723979e+00,-5.24773191e+00,-4.16018519e+00,5.90485168e+00,2.24577945e-01],[2.57793199e+00,-1.02752714e+00,-1.18857905e+00,9.93868795e-01,-2.40504439e+00,4.50551091e-01,-1.83198312e+00,-1.51552597e+00,1.97739950e+00,4.59946055e-01],[1.17304533e+00,-4.27095368e-01,-5.12203723e-01,6.40457782e-01,-1.07293721e+00,1.57396685e-01,-8.23116569e-01,-6.27740034e-01,9.58451406e-01,4.43934047e-01],[8.01916501e+00,-3.55740198e+00,-3.49352226e+00,3.60637634e+00,-7.50330094e+00,1.20691246e+00,-5.81507688e+00,-4.71535779e+00,6.48777272e+00,1.18965298e+00],[1.34198132e+00,-7.67962424e-01,-6.80867247e-01,4.52662015e-01,-1.40150602e+00,1.38654248e-01,-9.67822516e-01,-8.27290049e-01,1.38135094e+00,-2.98017845e-01],[5.01468485e+00,-2.23225160e+00,-2.20266748e+00,2.41078416e+00,-4.56743107e+00,7.99109014e-01,-3.59221915e+00,-2.93062437e+00,4.00802765e+00,3.16349773e-01],[4.25528635e+00,-1.94794312e+00,-1.91870614e+00,2.60376811e+00,-3.88313312e+00,6.63568308e-01,-3.00182601e+00,-2.50257263e+00,3.49076033e+00,-2.41433760e+00],[5.84819155e+00,-3.13137558e+00,-2.55829700e+00,2.13760329e+00,-5.45026549e+00,9.25897777e-01,-4.24463228e+00,-3.40256329e+00,4.67418593e+00,2.33146169e+00],[1.54921869e+00,-1.54841497e+00,-7.32459781e-01,1.07342250e-01,-1.49279467e+00,2.47370827e-01,-1.07855541e+00,-1.01438414e+00,1.39161006e+00,-4.43044278e+00],[5.38319928e+00,-2.70984793e+00,-2.37671510e+00,2.13814913e+00,-5.13122555e+00,8.29652453e-01,-3.80328670e+00,-3.24100432e+00,4.48328284e+00,2.73585377e+00],[1.05404485e+00,-4.47670627e-01,-4.95493343e-01,4.40723844e-01,-9.11988838e-01,1.58550131e-01,-7.86861155e-01,-6.13594176e-01,8.55489879e-01,7.57290181e-01],[1.20036462e+00,-4.19631317e-01,-5.52968784e-01,-4.12589787e-01,-1.19858038e+00,2.39171720e-01,-8.71038254e-01,-7.59278447e-01,1.05605508e+00,3.91789133e+00],[-1.06370758e+00,5.24805588e-01,4.24035581e-01,-2.79863740e-01,1.01353927e+00,-9.90872328e-02,7.44745444e-01,6.20823256e-01,-8.61020589e-01,1.65599031e+00],[5.77184391e-01,-3.81463582e-01,-2.80472186e-01,4.29976006e-01,-6.08658453e-01,1.70415318e-01,-3.99183809e-01,-3.82966704e-01,5.55891187e-01,-1.34775052e-02],[7.27989303e+00,-3.63494046e+00,-3.31837749e+00,3.17492850e+00,-6.78626127e+00,1.02225196e+00,-5.19481597e+00,-4.35770780e+00,5.99494349e+00,2.89413861e+00],[3.86076594e-01,-3.10934502e-01,-2.18238615e-01,2.24591241e-01,-3.81641308e-01,6.06251904e-02,-3.29517645e-01,-3.28215029e-01,4.81227048e-01,-1.10908322e-01],[6.23375202e+00,-3.02289096e+00,-2.76564954e+00,1.30916903e+00,-6.00298631e+00,9.13709815e-01,-4.42583479e+00,-3.73006191e+00,5.19595122e+00,7.91554836e-01],[1.03278354e+00,-5.25575445e-01,-5.44758716e-01,5.25827686e-01,-1.07962935e+00,1.26931736e-01,-6.79774860e-01,-7.12562490e-01,1.03554490e+00,-3.71147071e-01],[3.18039572e+00,-1.22553995e+00,-1.36090837e+00,1.64801276e+00,-2.97782013e+00,4.59847591e-01,-2.27363193e+00,-1.89061729e+00,2.50937227e+00,-3.26717920e-01],[4.49482886e+00,-2.26455112e+00,-2.05227594e+00,3.77611945e+00,-4.15147986e+00,6.42394235e-01,-3.10834877e+00,-2.56742140e+00,3.73322732e+00,-6.37838974e+00],[2.07129845e-01,-9.85907214e-02,-1.24829037e-01,-3.90480970e-02,-1.72900924e-01,-1.58098363e-02,-8.01889923e-02,-9.02655930e-02,1.35221282e-01,1.07638295e+00],[3.89465019e+00,-1.78327287e+00,-1.80448714e+00,2.37915102e+00,-3.68370609e+00,5.80860902e-01,-2.76885534e+00,-2.27832221e+00,3.17788430e+00,1.88277892e-02],[1.18602002e+00,-8.21266037e-01,-5.56358720e-01,-9.92556879e-01,-1.11593736e+00,9.65849104e-02,-8.21791891e-01,-8.22274679e-01,1.16613854e+00,3.30055761e+00],[2.12514394e+00,-9.36681992e-01,-9.91668535e-01,1.46303220e+00,-2.03715826e+00,3.14670865e-01,-1.57785465e+00,-1.23411691e+00,1.72619813e+00,-5.80084005e-02],[1.40705996e+00,-8.94634973e-02,-6.05965031e-01,-8.25885867e-02,-1.32447190e+00,2.93486237e-01,-1.13122120e+00,-8.21419188e-01,1.17011007e+00,4.66004507e+00],[-1.79862920e+00,-4.15226965e-01,3.47744047e-01,3.30998654e+00,6.63917359e-01,-1.73753844e+00,-3.69102446e-01,1.47971124e+00,-2.21355771e+00,5.51136263e+00],[6.92675704e+00,-3.78918419e+00,-3.59857198e+00,5.68215103e+00,-7.42929551e+00,-3.59499250e-01,-6.48321358e+00,-3.47968381e+00,4.54824225e+00,5.46119854e-02],[-3.18978823e+00,-6.35767454e-01,8.66740886e-01,9.24444401e-01,2.00003466e+00,-2.03743369e+00,6.88345811e-01,2.13580099e+00,-3.35060339e+00,7.94669011e-01],[-2.18987365e+01,1.15834800e+01,9.52397605e+00,-3.31718605e+00,2.05579796e+01,-4.87731437e+00,1.47061188e+01,1.42238077e+01,-2.04192234e+01,3.17067520e+00],[9.81404559e+00,-7.61116663e+00,-5.62668188e+00,2.68725584e+00,-1.20486861e+01,-9.91018215e-01,-9.26017977e+00,-6.99683062e+00,1.03705606e+01,-1.32901088e-01],[-3.07041987e+01,5.40307377e+00,1.25072916e+01,3.35144527e+00,2.75036135e+01,-1.03332736e+01,2.13861637e+01,1.65619017e+01,-2.18346670e+01,-5.58896939e+00],[1.61733159e+01,3.03143734e+00,-7.18575086e+00,4.95279251e+00,-1.56485002e+01,5.51143985e+00,-1.56382744e+01,-6.97183115e+00,1.04832272e+01,-6.30071629e+00],[2.88880494e+00,-7.13674494e+00,-1.89012511e+00,-1.12181618e+00,-3.74049222e+00,2.55331548e-01,-1.91356192e+00,-3.29388128e+00,4.81908179e+00,-1.01964919e+00],[-8.58521606e+01,2.95406882e+01,3.68418036e+01,-2.58196050e+01,7.81938825e+01,-1.67419000e+01,5.91601522e+01,5.00117771e+01,-6.92950661e+01,-6.68692274e-01],[5.80472588e+01,-2.52465495e+01,-2.67730482e+01,5.15101760e+00,-5.59331347e+01,8.63600434e+00,-4.44105154e+01,-3.42325429e+01,4.77467207e+01,4.69735808e-01],[3.28491868e+00,5.49236400e+00,-3.15294199e+00,-5.96423821e-01,-6.77163225e+00,2.30437776e+00,-4.46376342e+00,-2.96971107e+00,5.82858578e+00,5.87821462e-02],[-6.27084887e+00,-2.55654968e+00,1.85940979e+00,5.33296552e-01,4.14557343e+00,-2.36468185e+00,2.92114593e+00,3.01662215e+00,-4.49804527e+00,2.54145211e-02],[-6.88963629e+01,2.13319546e+01,2.94507911e+01,-1.06963766e+01,6.27651818e+01,-1.57967055e+01,4.89254854e+01,3.87985978e+01,-5.27461187e+01,2.07338913e-01],[-3.21254533e+00,1.11531181e+00,1.31081194e+00,-2.56616422e+00,2.95121863e+00,-3.95995317e-01,2.26640335e+00,1.79430970e+00,-2.33384524e+00,4.08590319e+00],[-1.13670281e+02,3.50996566e+01,4.94492032e+01,-2.40575417e+01,1.03614363e+02,-2.62405292e+01,8.60097466e+01,5.92336198e+01,-7.94074234e+01,-1.09989528e+00],[8.98703025e+00,-5.66160212e-01,-4.44249115e+00,-6.43652436e-01,-9.09091030e+00,2.85746893e+00,-7.58151491e+00,-4.83973975e+00,8.06424265e+00,1.96664495e-01],[-1.76438338e+01,8.57074814e+00,8.12883727e+00,-1.13741758e+01,1.73271791e+01,-1.02102133e+00,1.19305272e+01,1.17503626e+01,-1.71969032e+01,8.78553769e+00],[-1.27979015e+00,-5.96519917e-01,9.04667846e-03,3.83901743e+00,2.95187289e-01,-1.62518607e+00,-7.88254311e-01,1.06567878e+00,-1.78440593e+00,-1.41775739e+00],[-1.10271349e+00,-6.62784591e-01,-8.75269267e-02,3.91665864e+00,2.57998758e-02,-1.66166225e+00,-8.11208060e-01,1.08137560e+00,-1.62728405e+00,-1.51183797e+00],[-2.36883190e-01,-8.61535062e-01,-4.36132920e-01,4.11126418e+00,-7.15448490e-01,-1.42306954e+00,-1.41525097e+00,5.40613617e-01,-1.03243036e+00,1.07752226e-01],[-1.66181443e+00,-4.04764786e-01,2.35031220e-01,3.75943116e+00,6.24450535e-01,-1.68035911e+00,-4.21829573e-01,1.26006862e+00,-2.08625427e+00,-1.13388199e+00],[-5.38533842e+00,9.88300508e-01,1.91525798e+00,2.97171030e+00,4.15449415e+00,-2.12461055e+00,2.39113909e+00,3.41602434e+00,-5.05019714e+00,1.78620062e-01],[-2.45554331e+00,5.89185318e-02,5.93573894e-01,3.05412501e+00,1.49856457e+00,-1.84248595e+00,1.75394726e-01,1.82840441e+00,-2.92371749e+00,1.29559771e+01],[-5.81164431e+00,1.20463257e+00,2.01201197e+00,2.94329805e+00,4.43268980e+00,-2.26967988e+00,2.58765551e+00,3.62709766e+00,-5.35061137e+00,4.44210664e-01],[-5.82848105e+00,1.16376569e+00,1.97091773e+00,2.87705026e+00,4.45041272e+00,-2.20361447e+00,2.57155721e+00,3.59758840e+00,-5.30346335e+00,6.05258684e-01],[3.46948138e+00,-2.32398246e+00,-2.09166966e+00,6.60469142e+00,-4.23474287e+00,-9.04037340e-01,-4.26152686e+00,-1.50736911e+00,1.82456214e+00,-5.95442501e+00]]),([[-3.59244603,8.84754662,19.30445419,9.96253692,9.73465693],[-21.55594574,20.54918757,30.32761477,31.78497095,21.94020513],[-0.19503803,-1.97212312,-1.81520019,2.30880372,-2.58982919],[3.50107365,-17.83567502,-15.52560472,-17.36607349,-15.5614889],[2.18902126,-5.51756265,-4.88500505,-0.3649104,-5.14310902],[1.31486037,5.46834935,13.26335722,3.91312062,5.63666823],[12.90335978,-8.24065189,-9.86854943,-13.93469037,-9.21906667],[-6.59912767,9.09476329,12.08337214,14.07188809,8.73090044],[13.04241761,-21.33470057,-20.9479761,-27.41170429,-21.04769517],[-8.81924394,4.58408036,21.93518169,35.32536556,11.83849522]]),([[-16.34933265],[-13.33294193],[-5.04803898],[26.01300374],[-17.52598447]])]
    
    Input = Values
    InputX = []
    for i in range(len(coefs_)):
        coef_Inner = coefs_[i]
        intercepts = intercepts_[i]
        if(i!=0):
            Input = InputX
            InputX = []
        for j in range(len(intercepts)):                    
            for l in range(len(coef_Inner[j])):
                layer = 0
                for m in range(len(Input)):
                    layer = layer+(coef_Inner[m][j]*Input[m])                        
                X=layer+intercepts[j]
            X = 1/(1+(2.718**-X))
            InputX.append(X)
    return InputX

def C2BIP3(string):
    if sys.version_info[0] > 2:
        return bytes([ord(x) for x in string])
    else:
        return string
#%%
