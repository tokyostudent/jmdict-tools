package DB;

import DataModel.Entry;
import org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException;

import java.io.InterruptedIOException;

public interface IBuilder {
    void Add(Entry e) throws InterruptedIOException, RetriesExhaustedWithDetailsException;
}
