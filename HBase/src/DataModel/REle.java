package DataModel;

import lombok.Getter;
import lombok.Setter;
import org.apache.hadoop.hbase.util.Bytes;

import javax.xml.namespace.QName;
import java.util.ArrayList;
import java.util.List;

public class REle {

    public static final QName TAG_NAME = new QName("r_ele");
    public static final QName REB_TAG_NAME = new QName("reb");
    public static final QName RE_RESTR_TAG_NAME = new QName("re_restr");


    @Getter
    @Setter
    private String reb;

    @Getter
    private List<String> reRestrList = new ArrayList<String>();

    public Boolean isReadingFor(KEle k_ele)
    {
        //current r_ele has reading for a given keb if re_restr does not exist at all
        //or it contains the keb

        return getReRestrList().isEmpty() || getReRestrList().contains(k_ele.getKeb());

    }

    public byte[] toBytes()
    {
        return Bytes.toBytes(reb);
    }

}
