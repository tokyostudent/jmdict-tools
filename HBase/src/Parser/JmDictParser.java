package Parser;

import DataModel.*;
import org.codehaus.stax2.XMLInputFactory2;
import org.codehaus.stax2.XMLStreamReader2;

import javax.xml.namespace.QName;
import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.events.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Iterator;

public class JmDictParser implements IJMDictParser {
    private final XMLEventReader _eventReader;

    public JmDictParser(String jmDictXmlLocation) throws FileNotFoundException, XMLStreamException {
//        String filename = "/Users/oleglevy/PycharmProjects/hbasing/jm-tiny.xml";

        XMLInputFactory2 xmlif = (XMLInputFactory2)XMLInputFactory2.newInstance();
        XMLStreamReader2 xmlr =
                (XMLStreamReader2)
                        xmlif.createXMLStreamReader(
                                jmDictXmlLocation, new
                                FileInputStream(jmDictXmlLocation));


        _eventReader = xmlif.createXMLEventReader(xmlr);
    }

    @Override
    public void Start(IParserEvents client) throws XMLStreamException {
        Entry tempEntry = null;
        KEle tempkEle = null;
        REle temprEle = null;
        Attribute glossLang = null;
        Sense tempSense = null;
        Characters tempChars = null;
        Iterator glossAttributes = null;

        while (_eventReader.hasNext())
        {
            XMLEvent nextEvent = _eventReader.nextEvent();


            if (nextEvent.isStartElement())
            {
                StartElement startElement = nextEvent.asStartElement();
                QName startTag = startElement.getName();

                if (startTag.equals(Entry.TAG_NAME))
                    tempEntry = new Entry();
                else if (startTag.equals(KEle.TAG_NAME))
                    tempEntry.getKEleList().add(tempkEle = new KEle());
                else if (startTag.equals(REle.TAG_NAME))
                    tempEntry.getREleList().add(temprEle = new REle());
                else if (startTag.equals(Sense.TAG_NAME))
                    tempEntry.getSenseList().add(tempSense = new Sense());
                else if (startTag.equals(Gloss.TAG_NAME))
                    glossLang = startElement.getAttributeByName(new QName("http://www.w3.org/XML/1998/namespace", "lang"));


            }
            else if (nextEvent.isEndElement())
            {
                EndElement endElement = nextEvent.asEndElement();
                QName endTag = endElement.getName();

                if (endTag.equals(KEle.KEB_TAG_NAME))
                    tempkEle.setKeb(tempChars.getData());

                else if (endTag.equals(REle.REB_TAG_NAME))
                    temprEle.setReb(tempChars.getData());

                else if (endTag.equals(REle.RE_RESTR_TAG_NAME))
                    temprEle.getReRestrList().add(tempChars.getData());

                else if (endTag.equals(Entry.TAG_NAME))
                    client.EntryParsed(tempEntry);

                else if (endTag.equals(Sense.STAGK_TAG_NAME))
                    tempSense.getStagkList().add(tempChars.getData());

                else if (endTag.equals(Sense.STAGR_TAG_NAME))
                    tempSense.getStagrList().add(tempChars.getData());

                else if (endTag.equals(Gloss.TAG_NAME)){
                    final String lang = (null != glossLang) ? glossLang.getValue() : "eng";
                    tempSense.getGlossList().add(new Gloss(tempChars.getData(), lang));

                }
            }

            if (nextEvent.isCharacters())
            {
                tempChars = nextEvent.asCharacters();

            }


        }

        client.ParsingFinished();

    }
}
