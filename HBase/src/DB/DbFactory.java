package DB;

import java.io.IOException;

public class DbFactory {
    public static IBuilder createHBaseBuilder(String tableName) throws IOException {
        return new HBaseBuilderImpl(tableName);
    }
}
