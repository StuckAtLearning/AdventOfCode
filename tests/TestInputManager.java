import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InputManagerTest {
    @Test
    public void testReadFile() {
        List<String> testFileInfo = InputManager.readFile(Path.of("tests/double_new_line_int_only.txt"));
        String[] expectedOutputTemp = {"9686", "10178", "3375", "9638", "", "24919", "15983", "18045", "", "24872", "35761"};
        List<String> expectedOutput = Arrays.asList(expectedOutputTemp);
        Assertions.assertEquals(expectedOutput,testFileInfo);
    }

    @Test
    public void testGroupFileWithDoubleNewLine() {
        String testFileInfo = "9686\n10178\n3375\n9638\n\n24919\n15983\n18045\n\n24872\n35761";
        String[][] expectedOutputTemp = {{"9686", "10178", "3375", "9638"}, {"24919", "15983", "18045"}, {"24872", "35761"}};
        List<List<String>> expectedOutput = Arrays.stream(expectedOutputTemp).map(Arrays::asList).toList();
        Assertions.assertEquals(expectedOutput,testFileInfo);
    }
}
