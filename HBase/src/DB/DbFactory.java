package DB;

import java.io.IOException;

public class DbFactory {
    public static IBuilder createHBaseBuilder(String tableName) throws IOException {
        return new HBaseBuilderImpl(tableName, true);
    }

    public static IBuilder createHBaseBuilder(String tableName, Boolean recreateTables) throws IOException {
        return new HBaseBuilderImpl(tableName, recreateTables);
    }
}
