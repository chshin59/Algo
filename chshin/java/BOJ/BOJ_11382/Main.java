// BOJ_11382 꼬마 정민
package BOJ.BOJ_11382;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long result = 0;
        for (int i = 0; i < 3; i++) {
            result += Long.parseLong(st.nextToken());
        }
        System.out.println(result);
    }
}
