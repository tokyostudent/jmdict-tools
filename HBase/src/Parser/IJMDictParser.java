package Parser;

import javax.xml.stream.XMLStreamException;

/**
 * Created by oleglevy on 10/16/13.
 */
public interface IJMDictParser {
    void Start(IParserEvents client) throws XMLStreamException;
}
