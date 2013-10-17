package DataModel;

import lombok.Getter;
import lombok.Setter;
import org.apache.hadoop.hbase.util.Bytes;

import javax.xml.namespace.QName;
import java.util.ArrayList;
import java.util.List;

public class KEle {
    public static final QName KEB_TAG_NAME = new QName("keb");
    public static final QName TAG_NAME=new QName("k_ele");


    @Getter @Setter
    private String keb;

    @Getter
    private List<String> kInfList = new ArrayList<String>();

    @Getter
    private List<String> kPriList = new ArrayList<String>();

    public byte[] toBytes()
    {
        return Bytes.toBytes(keb);
    }
}
