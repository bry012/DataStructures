__author__ = 'bryan'
from Stack import Stack
import re

def convert_xml_to_string(path):
    f = open(path,"r")
    xmlString = "".join(f.readlines())
    return xmlString


def compare_tags(opening,close):
    opening = opening.split(" ")[0].strip()
    if ">" not in opening:
        opening += ">"
    close = re.sub("/","",close).strip()
    if opening == close:
        print("valid")
    else:
        print("invalid")
        print(opening, re.sub("<","</",close))

def create_line(charStack, currentTag):
    while charStack.isEmpty() != True:
                currentTag = charStack.pop() + currentTag
    return currentTag

def add_tabs(currentDepth, currentTag):
    currentTag = "\t"*currentDepth + currentTag
    return currentTag


def isSelfClosing(tag):
    tag = re.sub(" ","",tag)
    return "/>" in tag

def parseXML(xmlString):

    charStack = Stack()
    currentTag = ""
    tagStack = Stack()
    xmlList = []
    currentDepth = 0
    endTag = False

    for char in xmlString:
        if char == "<":
             currentTag = create_line(charStack, currentTag)
             currentTag = add_tabs(currentDepth, currentTag)
             xmlList.append(currentTag)
             currentTag = ""
             charStack.push(char)

        elif char == ">":
            currentTag += ">"
            currentTag = create_line(charStack,currentTag)
            currentTag = add_tabs(currentDepth, currentTag)

            if not endTag:
                tagStack.push(currentTag)
            elif not tagStack.isEmpty() and endTag:
                if not isSelfClosing(currentTag):
                    compare_tags(tagStack.pop(), currentTag)
                else:
                    currentDepth += 1
                    currentTag = add_tabs(currentDepth + 1, currentTag)
                endTag = False
            xmlList.append(currentTag)
            currentDepth += 1
            currentTag = ""
        elif char == "/":
            endTag = True
            if currentDepth != 1:
                chars = ""
                holdString = "\t"
                #loop to add tab in front of closing tags
                while chars != "<":
                    #checks for tags with anything but space between closing < and /
                    if chars.strip() != "":
                        holdString = chars
                        break
                    else:
                        chars = charStack.pop()
                        holdString += chars
                for x in holdString:
                    charStack.push(x)
            #ensure proper tag alignment
            currentDepth -= 2
            charStack.push(char)
        else:
            if char == "\n":
                char = " "
            charStack.push(char)
    #removes unneeded whitespace
    return [x for x in xmlList if x.strip() != ""]


for x in parseXML(convert_xml_to_string("test.xml")):
    print(x)




