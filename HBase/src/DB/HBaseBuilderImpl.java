package DB;

import DataModel.Entry;
import DataModel.KEle;
import DataModel.REle;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;

import java.io.IOException;
import java.util.List;

public class HBaseBuilderImpl implements IBuilder {
    private final HTable _table;
    HBaseBuilderImpl(String tableName) throws IOException {
        Configuration config = HBaseConfiguration.create();

        _table = new HTable(config, tableName);
    }

    @Override
    public void Add(Entry e) {

        for (KEle k_ele: e.getKEleList())
        {
            List<REle> rebs = e.getRebs(k_ele);



        }


    }


}
