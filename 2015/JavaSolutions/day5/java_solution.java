import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Day5 {
    private static final String[] DisallowedSubstring = {"ab", "cd", "pq", "xy"};
    private static final String Vowels = "aeiou";

    public static void main(String[] args) {
        List<String> inputFile = InputManager.readFile(Path.of("inputs/day_5_real_input.txt"));
        int part1Answer = getNiceStringsNum(inputFile);
        int part2Answer = getBetterStringNum(inputFile);
        System.out.println(part1Answer);
        System.out.println(part2Answer);
    }

    public static boolean checkAllowedSubstringOnly(String currentInput) {
        for (String subString: DisallowedSubstring) {
            if (currentInput.contains(subString)) {
                return false;
            }
        }
        return true;
    }

    public static boolean checkDoubleLetter(String currentInput) {
        for (int i = 0; i < currentInput.length()-1; i++) {
            if (currentInput.charAt(i) == currentInput.charAt(i+1)) {
                return true;
            }
        }
        return false;
    }

    public static boolean checkVowels(String currentInput) {
        int countVowels = 0;
        for (char letter: currentInput.toCharArray()) {
            if (Vowels.contains(String.valueOf(letter))) {
                countVowels ++;
            }
        }
        return countVowels > 2;
    }

    public static int getNiceStringsNum(List<String> allInputs) {
        int niceStringNum = 0;
        for (String input: allInputs) {
            if (checkVowels(input) && checkDoubleLetter(input) && checkAllowedSubstringOnly(input)) {
                niceStringNum ++;
            }
        }
        return niceStringNum;
    }

    public static boolean checkPairs(String currentInput) {
        for (int i = 2; i < currentInput.length(); i ++) {
            String check = currentInput.substring(i-1, i+1);
            String beforeCheck = currentInput.substring(0, i-1);
            String afterCheck = currentInput.substring(i+1);
            if (beforeCheck.contains(check) || afterCheck.contains(check)) {
                return true;
            }
        }
        return false;
    }

    public static boolean checkSandwichLetter(String currentInput) {
        char[] alphabetLower = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        for (char alphabet: alphabetLower) {
            Pattern pattern = Pattern.compile("[a-z]*%s.%s[a-z]*".formatted(alphabet, alphabet));
            Matcher matcher = pattern.matcher(currentInput);
            if (matcher.find()) {
                return true;
            }
        }
        return false;
    }

    public static int getBetterStringNum(List<String> allInputs) {
        int betterStringNum = 0;
        for (String input: allInputs) {
            if (checkPairs(input) && checkSandwichLetter(input)) {
                betterStringNum ++;
            }
        }
        return betterStringNum;
    }
}
