import java.util.HashMap;
import java.util.Map;

/**
 * Run: javac HashMapInternalsDemo.java && java HashMapInternalsDemo
 *
 * Shows hashCode(), HashMap's spread hash, and bucket index (same math as real HashMap).
 */
public class HashMapInternalsDemo {

    // Same idea as java.util.HashMap.hash(Object key)
    static int hashMapHash(Object key) {
        if (key == null) return 0;
        int h = key.hashCode();
        return h ^ (h >>> 16);
    }

    // Bucket index when table length is power of 2 (default capacity 16)
    static int bucketIndex(int hash, int capacity) {
        return (capacity - 1) & hash;
    }

    public static void main(String[] args) {
        int capacity = 16; // default HashMap size

        System.out.println("=== 1. String keys ===\n");
        printKeyInfo("John", capacity);
        printKeyInfo("Emma", capacity);

        System.out.println("\n=== 2. HashMap put / get ===\n");
        Map<String, String> map = new HashMap<>();
        map.put("John", "Dev");
        map.put("Emma", "QA");
        System.out.println("map.get(\"John\") = " + map.get("John"));
        System.out.println("map.size()       = " + map.size());

        System.out.println("\n=== 3. Employee keys (custom hashCode) ===\n");
        Employee e1 = new Employee(101, "Basant");
        Employee e2 = new Employee(102, "Peter");
        printKeyInfo(e1, capacity);
        printKeyInfo(e2, capacity);

        Map<Employee, String> empMap = new HashMap<>();
        empMap.put(e1, "Dev");
        empMap.put(e2, "QA");
        System.out.println("empMap.get(e1) = " + empMap.get(e1));

        System.out.println("\n=== 4. Same bucket (collision) — two different keys, same index ===\n");
        // These strings are chosen so they land in the same bucket for capacity 16
        String a = "Aa";
        String b = "BB";
        int idxA = bucketIndex(hashMapHash(a), capacity);
        int idxB = bucketIndex(hashMapHash(b), capacity);
        System.out.println("Key \"" + a + "\" -> bucket " + idxA);
        System.out.println("Key \"" + b + "\" -> bucket " + idxB);
        System.out.println("Collision? " + (idxA == idxB));

        Map<String, String> collisionMap = new HashMap<>();
        collisionMap.put(a, "value-Aa");
        collisionMap.put(b, "value-BB");
        System.out.println("Both stored: size=" + collisionMap.size()
                + ", get(Aa)=" + collisionMap.get(a)
                + ", get(BB)=" + collisionMap.get(b));

        System.out.println("\n=== 5. Replace value (same key, equals true) ===\n");
        Map<String, String> m = new HashMap<>();
        m.put("John", "Dev");
        System.out.println("After put John=Dev: " + m);
        m.put("John", "Lead");
        System.out.println("After put John=Lead (replace): " + m);
    }

    static void printKeyInfo(Object key, int capacity) {
        int raw = key.hashCode();
        int spread = hashMapHash(key);
        int bucket = bucketIndex(spread, capacity);
        System.out.println("Key: " + key);
        System.out.println("  hashCode()              = " + raw);
        System.out.println("  HashMap spread hash     = " + spread);
        System.out.println("  bucket index (size " + capacity + ") = " + bucket);
        System.out.println();
    }

    static class Employee {
        final int id;
        final String name;

        Employee(int id, String name) {
            this.id = id;
            this.name = name;
        }

        @Override
        public int hashCode() {
            return Integer.hashCode(id);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Employee)) return false;
            Employee other = (Employee) o;
            return id == other.id;
        }

        @Override
        public String toString() {
            return "Employee{id=" + id + ", name='" + name + "'}";
        }
    }
}
