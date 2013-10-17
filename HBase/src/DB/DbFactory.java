package DB;

/**
 * Created by oleglevy on 10/16/13.
 */
public class DbFactory {
    public static IBuilder createHBaseBuilder(String tableName)
    {
        return new HBaseBuilderImpl(tableName);
    }
}
