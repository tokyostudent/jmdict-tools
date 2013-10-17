import DataModel.Entry;
import Parser.IJMDictParser;
import Parser.IParserEvents;
import Parser.JmDictParserFactory;
import org.apache.commons.cli.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException;
import org.apache.hadoop.hbase.util.Bytes;

import javax.xml.stream.XMLStreamException;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InterruptedIOException;

public class Main {
    private static final String JMDICT_LOCATION_CMD_OPTION = "jmdictlocation";

    private static CommandLine checkCommandLine(String[] argv) throws ParseException {
        Options commandLineOptions = new Options();
        commandLineOptions.addOption(JMDICT_LOCATION_CMD_OPTION, true, "location of the jmdict.xml file");

        CommandLineParser parser = new BasicParser();
        return parser.parse(commandLineOptions, argv);
    }

    public static void main(String argv[]) throws FileNotFoundException, XMLStreamException, ParseException {
        CommandLine commandLine = checkCommandLine(argv);

//        String filename = "/Users/oleglevy/PycharmProjects/hbasing/jm-tiny.xml";


        IJMDictParser parser = JmDictParserFactory.createJmDictParser(commandLine.getOptionValue(JMDICT_LOCATION_CMD_OPTION));
        parser.Start(new IParserEvents() {
            @Override
            public void EntryParsed(Entry e) {
                System.out.println("Parsed something...");
            }

            @Override
            public void ParsingFinished() {
                System.out.println("Finished parsing...");
            }
        });





/*


        try {

            for (int i = 0; i < 1000; i++)
            {
                Put newPut = new Put(Bytes.toBytes("かな" + Math.random()));
                newPut.add(Bytes.toBytes("f1"), Bytes.toBytes("q1"), null);
                testTable.put(newPut);

            }


        } catch (InterruptedIOException e) {
            e.printStackTrace();
        } catch (RetriesExhaustedWithDetailsException e) {
            e.printStackTrace();
        }
*/

    }


}
