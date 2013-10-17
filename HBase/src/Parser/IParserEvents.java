package Parser;

import DataModel.Entry;

public interface IParserEvents {
    void EntryParsed(Entry e);

    void ParsingFinished();
}
