package DB;

import DataModel.Entry;
import DataModel.KEle;
import DataModel.REle;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;
import java.io.InterruptedIOException;
import java.util.LinkedList;
import java.util.List;

public class HBaseBuilderImpl implements IBuilder {
    private static final byte[] REBS_FAMILY = Bytes.toBytes("rebs");
    private static final byte[] KEBS_FAMILY = Bytes.toBytes("kebs");


    private final HTable _table;
    private final Configuration _config;
    private final String _tableName;

    HBaseBuilderImpl(String tableName, Boolean recreateTables) throws IOException {
        _config = HBaseConfiguration.create();
        _tableName = tableName;

        if (recreateTables)
            prepareTables();

        _table = new HTable(_config, _tableName);
    }

    private void prepareTables() throws IOException {
        HBaseAdmin admin = new HBaseAdmin(_config);

        try
        {
            //assume that the new table name is the same as old
            admin.deleteTable(_tableName);
        }
        catch (TableNotFoundException tableNotFoundException){}


        HTableDescriptor descriptor = new HTableDescriptor(TableName.valueOf(_tableName));

        descriptor.addFamily(new HColumnDescriptor(REBS_FAMILY));
        descriptor.addFamily(new HColumnDescriptor(KEBS_FAMILY));

        admin.createTable(descriptor);
    }

    @Override
    public void Add(Entry e) throws InterruptedIOException, RetriesExhaustedWithDetailsException {

        List<Put> putsToPut = new LinkedList<Put>();
        for (KEle k_ele: e.getKEleList())
        {
            Put newPut = new Put(k_ele.toBytes());

            for (REle r_ele: e.getRebs(k_ele))
                newPut.add(REBS_FAMILY, r_ele.toBytes(), e.getSensesBytes(k_ele, r_ele));

            putsToPut.add(newPut);
        }

        for (REle r_ele: e.getREleList())
        {
            Put newPut = new Put(r_ele.toBytes());

            for (KEle k_ele: e.getKebs(r_ele))
                newPut.add(KEBS_FAMILY, k_ele.toBytes(), e.getSensesBytes(k_ele, r_ele));

            putsToPut.add(newPut);
        }


        _table.put(putsToPut);
    }


}
