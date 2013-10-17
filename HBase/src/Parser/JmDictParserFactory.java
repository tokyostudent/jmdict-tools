package Parser;

import javax.xml.stream.XMLStreamException;
import java.io.FileNotFoundException;

public class JmDictParserFactory {
    public static IJMDictParser createJmDictParser(String jmDictXmlLocation) throws FileNotFoundException, XMLStreamException {
        return new JmDictParser(jmDictXmlLocation);
    }
}
