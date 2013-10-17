import DB.DbFactory;
import DB.IBuilder;
import DataModel.Entry;
import Parser.IJMDictParser;
import Parser.IParserEvents;
import Parser.JmDictParserFactory;
import org.apache.commons.cli.*;
import org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException;

import javax.xml.stream.XMLStreamException;
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

    public static void main(String argv[]) throws IOException, XMLStreamException, ParseException {
        CommandLine commandLine = checkCommandLine(argv);

//        String filename = "/Users/oleglevy/PycharmProjects/hbasing/jm-tiny.xml";


        final IJMDictParser parser = JmDictParserFactory.createJmDictParser(commandLine.getOptionValue(JMDICT_LOCATION_CMD_OPTION));
        final IBuilder hbaseBuilder = DbFactory.createHBaseBuilder("jmdict");


        parser.Start(new IParserEvents() {
            @Override
            public void EntryParsed(Entry e) {
                try
                {
                    hbaseBuilder.Add(e);
                }
                catch (RetriesExhaustedWithDetailsException e1) {
                    e1.printStackTrace();
                } catch (InterruptedIOException e1) {
                    e1.printStackTrace();
                }
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
