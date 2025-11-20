# 🏗️ Design Patterns in Java

Master Gang of Four patterns and modern Java design patterns!

---

## 📚 Table of Contents

1. [Creational Patterns](#creational-patterns)
2. [Structural Patterns](#structural-patterns)
3. [Behavioral Patterns](#behavioral-patterns)
4. [Concurrency Patterns](#concurrency-patterns)
5. [Modern Java Patterns](#modern-patterns)
6. [Interview Questions](#interview-questions)

---

## 🎨 Creational Patterns

### Q1: Singleton Pattern (Thread-Safe)

**Answer:**

```java
// Approach 1: Eager Initialization
public class EagerSingleton {
    private static final EagerSingleton instance = new EagerSingleton();
    
    private EagerSingleton() {}
    
    public static EagerSingleton getInstance() {
        return instance;
    }
}

// Approach 2: Lazy Initialization with Double-Checked Locking
public class LazySingleton {
    private static volatile LazySingleton instance;
    
    private LazySingleton() {
        // Prevent reflection attack
        if (instance != null) {
            throw new IllegalStateException("Instance already created");
        }
    }
    
    public static LazySingleton getInstance() {
        if (instance == null) {
            synchronized (LazySingleton.class) {
                if (instance == null) {
                    instance = new LazySingleton();
                }
            }
        }
        return instance;
    }
}

// Approach 3: Bill Pugh Singleton (Best approach before enums)
public class BillPughSingleton {
    private BillPughSingleton() {}
    
    private static class SingletonHelper {
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }
    
    public static BillPughSingleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}

// Approach 4: Enum Singleton (BEST APPROACH)
public enum EnumSingleton {
    INSTANCE;
    
    private String data;
    
    public void setData(String data) {
        this.data = data;
    }
    
    public String getData() {
        return data;
    }
    
    public void businessMethod() {
        System.out.println("Executing business logic");
    }
}

// Usage
public class SingletonDemo {
    public static void main(String[] args) {
        // Enum singleton usage
        EnumSingleton singleton = EnumSingleton.INSTANCE;
        singleton.setData("Test data");
        singleton.businessMethod();
        
        // Same instance
        EnumSingleton anotherRef = EnumSingleton.INSTANCE;
        System.out.println(singleton == anotherRef); // true
    }
}
```

### Q2: Factory Pattern

**Answer:**

```java
// Product interface
interface Vehicle {
    void manufacture();
}

// Concrete products
class Car implements Vehicle {
    @Override
    public void manufacture() {
        System.out.println("Manufacturing a Car");
    }
}

class Bike implements Vehicle {
    @Override
    public void manufacture() {
        System.out.println("Manufacturing a Bike");
    }
}

class Truck implements Vehicle {
    @Override
    public void manufacture() {
        System.out.println("Manufacturing a Truck");
    }
}

// Factory class
class VehicleFactory {
    public static Vehicle createVehicle(String type) {
        return switch (type.toLowerCase()) {
            case "car" -> new Car();
            case "bike" -> new Bike();
            case "truck" -> new Truck();
            default -> throw new IllegalArgumentException("Unknown vehicle type: " + type);
        };
    }
}

// Usage
public class FactoryPatternDemo {
    public static void main(String[] args) {
        Vehicle car = VehicleFactory.createVehicle("car");
        car.manufacture();
        
        Vehicle bike = VehicleFactory.createVehicle("bike");
        bike.manufacture();
        
        Vehicle truck = VehicleFactory.createVehicle("truck");
        truck.manufacture();
    }
}
```

### Q3: Abstract Factory Pattern

**Answer:**

```java
// Abstract products
interface Button {
    void paint();
}

interface Checkbox {
    void paint();
}

// Concrete products - Windows
class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering Windows button");
    }
}

class WindowsCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("Rendering Windows checkbox");
    }
}

// Concrete products - Mac
class MacButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering Mac button");
    }
}

class MacCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("Rendering Mac checkbox");
    }
}

// Abstract factory
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// Concrete factories
class WindowsFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }
    
    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

class MacFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new MacButton();
    }
    
    @Override
    public Checkbox createCheckbox() {
        return new MacCheckbox();
    }
}

// Client code
class Application {
    private Button button;
    private Checkbox checkbox;
    
    public Application(GUIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
    }
    
    public void render() {
        button.paint();
        checkbox.paint();
    }
}

// Usage
public class AbstractFactoryDemo {
    public static void main(String[] args) {
        String os = "Windows"; // or "Mac"
        
        GUIFactory factory;
        if (os.equals("Windows")) {
            factory = new WindowsFactory();
        } else {
            factory = new MacFactory();
        }
        
        Application app = new Application(factory);
        app.render();
    }
}
```

### Q4: Builder Pattern

**Answer:**

```java
// Complex object
public class Computer {
    // Required parameters
    private final String CPU;
    private final String RAM;
    
    // Optional parameters
    private final String storage;
    private final String GPU;
    private final String motherboard;
    private final String powerSupply;
    private final boolean isWaterCooled;
    private final boolean hasRGB;
    
    private Computer(Builder builder) {
        this.CPU = builder.CPU;
        this.RAM = builder.RAM;
        this.storage = builder.storage;
        this.GPU = builder.GPU;
        this.motherboard = builder.motherboard;
        this.powerSupply = builder.powerSupply;
        this.isWaterCooled = builder.isWaterCooled;
        this.hasRGB = builder.hasRGB;
    }
    
    // Builder class
    public static class Builder {
        // Required parameters
        private final String CPU;
        private final String RAM;
        
        // Optional parameters - default values
        private String storage = "256GB SSD";
        private String GPU = "Integrated";
        private String motherboard = "Standard";
        private String powerSupply = "500W";
        private boolean isWaterCooled = false;
        private boolean hasRGB = false;
        
        public Builder(String CPU, String RAM) {
            this.CPU = CPU;
            this.RAM = RAM;
        }
        
        public Builder storage(String storage) {
            this.storage = storage;
            return this;
        }
        
        public Builder GPU(String GPU) {
            this.GPU = GPU;
            return this;
        }
        
        public Builder motherboard(String motherboard) {
            this.motherboard = motherboard;
            return this;
        }
        
        public Builder powerSupply(String powerSupply) {
            this.powerSupply = powerSupply;
            return this;
        }
        
        public Builder waterCooled(boolean isWaterCooled) {
            this.isWaterCooled = isWaterCooled;
            return this;
        }
        
        public Builder RGB(boolean hasRGB) {
            this.hasRGB = hasRGB;
            return this;
        }
        
        public Computer build() {
            return new Computer(this);
        }
    }
    
    @Override
    public String toString() {
        return "Computer{" +
                "CPU='" + CPU + '\'' +
                ", RAM='" + RAM + '\'' +
                ", storage='" + storage + '\'' +
                ", GPU='" + GPU + '\'' +
                ", motherboard='" + motherboard + '\'' +
                ", powerSupply='" + powerSupply + '\'' +
                ", isWaterCooled=" + isWaterCooled +
                ", hasRGB=" + hasRGB +
                '}';
    }
    
    public static void main(String[] args) {
        // Gaming PC
        Computer gamingPC = new Computer.Builder("Intel i9-13900K", "32GB DDR5")
                .storage("2TB NVMe SSD")
                .GPU("RTX 4090")
                .motherboard("ASUS ROG")
                .powerSupply("1000W")
                .waterCooled(true)
                .RGB(true)
                .build();
        
        System.out.println(gamingPC);
        
        // Office PC
        Computer officePC = new Computer.Builder("Intel i5-13400", "16GB DDR4")
                .storage("512GB SSD")
                .build();
        
        System.out.println(officePC);
    }
}
```

### Q5: Prototype Pattern

**Answer:**

```java
// Cloneable interface
abstract class Shape implements Cloneable {
    protected String type;
    private String id;
    
    abstract void draw();
    
    public String getType() {
        return type;
    }
    
    public String getId() {
        return id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
    
    @Override
    public Object clone() {
        Object clone = null;
        try {
            clone = super.clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        return clone;
    }
}

// Concrete prototypes
class Circle extends Shape {
    public Circle() {
        type = "Circle";
    }
    
    @Override
    void draw() {
        System.out.println("Drawing a Circle");
    }
}

class Rectangle extends Shape {
    public Rectangle() {
        type = "Rectangle";
    }
    
    @Override
    void draw() {
        System.out.println("Drawing a Rectangle");
    }
}

class Square extends Shape {
    public Square() {
        type = "Square";
    }
    
    @Override
    void draw() {
        System.out.println("Drawing a Square");
    }
}

// Shape cache
class ShapeCache {
    private static java.util.Hashtable<String, Shape> shapeMap = new java.util.Hashtable<>();
    
    public static Shape getShape(String shapeId) {
        Shape cachedShape = shapeMap.get(shapeId);
        return (Shape) cachedShape.clone();
    }
    
    public static void loadCache() {
        Circle circle = new Circle();
        circle.setId("1");
        shapeMap.put(circle.getId(), circle);
        
        Rectangle rectangle = new Rectangle();
        rectangle.setId("2");
        shapeMap.put(rectangle.getId(), rectangle);
        
        Square square = new Square();
        square.setId("3");
        shapeMap.put(square.getId(), square);
    }
}

// Usage
public class PrototypePatternDemo {
    public static void main(String[] args) {
        ShapeCache.loadCache();
        
        Shape clonedCircle = ShapeCache.getShape("1");
        System.out.println("Shape: " + clonedCircle.getType());
        clonedCircle.draw();
        
        Shape clonedRectangle = ShapeCache.getShape("2");
        System.out.println("Shape: " + clonedRectangle.getType());
        clonedRectangle.draw();
        
        Shape clonedSquare = ShapeCache.getShape("3");
        System.out.println("Shape: " + clonedSquare.getType());
        clonedSquare.draw();
    }
}
```

---

## 🔨 Structural Patterns

### Q6: Adapter Pattern

**Answer:**

```java
// Target interface
interface MediaPlayer {
    void play(String audioType, String fileName);
}

// Adaptee interfaces
interface AdvancedMediaPlayer {
    void playVlc(String fileName);
    void playMp4(String fileName);
}

// Concrete adaptees
class VlcPlayer implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        System.out.println("Playing VLC file: " + fileName);
    }
    
    @Override
    public void playMp4(String fileName) {
        // Do nothing
    }
}

class Mp4Player implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        // Do nothing
    }
    
    @Override
    public void playMp4(String fileName) {
        System.out.println("Playing MP4 file: " + fileName);
    }
}

// Adapter
class MediaAdapter implements MediaPlayer {
    private AdvancedMediaPlayer advancedPlayer;
    
    public MediaAdapter(String audioType) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedPlayer = new VlcPlayer();
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedPlayer = new Mp4Player();
        }
    }
    
    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedPlayer.playVlc(fileName);
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedPlayer.playMp4(fileName);
        }
    }
}

// Client
class AudioPlayer implements MediaPlayer {
    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("mp3")) {
            System.out.println("Playing MP3 file: " + fileName);
        } else if (audioType.equalsIgnoreCase("vlc") || 
                   audioType.equalsIgnoreCase("mp4")) {
            MediaAdapter adapter = new MediaAdapter(audioType);
            adapter.play(audioType, fileName);
        } else {
            System.out.println("Invalid format: " + audioType);
        }
    }
}

// Usage
public class AdapterPatternDemo {
    public static void main(String[] args) {
        AudioPlayer audioPlayer = new AudioPlayer();
        
        audioPlayer.play("mp3", "song.mp3");
        audioPlayer.play("mp4", "video.mp4");
        audioPlayer.play("vlc", "movie.vlc");
        audioPlayer.play("avi", "film.avi");
    }
}
```

### Q7: Decorator Pattern

**Answer:**

```java
// Component interface
interface Coffee {
    String getDescription();
    double getCost();
}

// Concrete component
class SimpleCoffee implements Coffee {
    @Override
    public String getDescription() {
        return "Simple Coffee";
    }
    
    @Override
    public double getCost() {
        return 2.0;
    }
}

// Decorator base class
abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;
    
    public CoffeeDecorator(Coffee coffee) {
        this.decoratedCoffee = coffee;
    }
    
    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }
    
    @Override
    public double getCost() {
        return decoratedCoffee.getCost();
    }
}

// Concrete decorators
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) {
        super(coffee);
    }
    
    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Milk";
    }
    
    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.5;
    }
}

class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee coffee) {
        super(coffee);
    }
    
    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Sugar";
    }
    
    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.2;
    }
}

class VanillaDecorator extends CoffeeDecorator {
    public VanillaDecorator(Coffee coffee) {
        super(coffee);
    }
    
    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Vanilla";
    }
    
    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.7;
    }
}

// Usage
public class DecoratorPatternDemo {
    public static void main(String[] args) {
        // Simple coffee
        Coffee coffee = new SimpleCoffee();
        System.out.println(coffee.getDescription() + " $" + coffee.getCost());
        
        // Coffee with milk
        Coffee milkCoffee = new MilkDecorator(new SimpleCoffee());
        System.out.println(milkCoffee.getDescription() + " $" + milkCoffee.getCost());
        
        // Coffee with milk, sugar, and vanilla
        Coffee fancyCoffee = new VanillaDecorator(
                                new SugarDecorator(
                                    new MilkDecorator(
                                        new SimpleCoffee())));
        System.out.println(fancyCoffee.getDescription() + " $" + fancyCoffee.getCost());
    }
}
```

### Q8: Proxy Pattern

**Answer:**

```java
// Subject interface
interface Image {
    void display();
}

// Real subject
class RealImage implements Image {
    private String filename;
    
    public RealImage(String filename) {
        this.filename = filename;
        loadFromDisk();
    }
    
    private void loadFromDisk() {
        System.out.println("Loading image: " + filename);
        // Simulate expensive operation
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    @Override
    public void display() {
        System.out.println("Displaying image: " + filename);
    }
}

// Proxy
class ProxyImage implements Image {
    private String filename;
    private RealImage realImage;
    
    public ProxyImage(String filename) {
        this.filename = filename;
    }
    
    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }
}

// Usage
public class ProxyPatternDemo {
    public static void main(String[] args) {
        System.out.println("=== Using Proxy ===");
        Image image1 = new ProxyImage("photo1.jpg");
        Image image2 = new ProxyImage("photo2.jpg");
        
        // Image loaded only when displayed
        System.out.println("\nFirst display:");
        image1.display();
        
        System.out.println("\nSecond display (cached):");
        image1.display();
        
        System.out.println("\nDisplaying another image:");
        image2.display();
    }
}
```

---

## 🎭 Behavioral Patterns

### Q9: Observer Pattern

**Answer:**

```java
import java.util.*;

// Subject interface
interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers();
}

// Observer interface
interface Observer {
    void update(String message);
}

// Concrete subject
class NewsAgency implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String news;
    
    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }
    
    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }
    
    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(news);
        }
    }
    
    public void setNews(String news) {
        this.news = news;
        notifyObservers();
    }
}

// Concrete observers
class NewsChannel implements Observer {
    private String name;
    
    public NewsChannel(String name) {
        this.name = name;
    }
    
    @Override
    public void update(String message) {
        System.out.println(name + " received news: " + message);
    }
}

class MobileApp implements Observer {
    private String appName;
    
    public MobileApp(String appName) {
        this.appName = appName;
    }
    
    @Override
    public void update(String message) {
        System.out.println("[" + appName + " Push Notification] " + message);
    }
}

// Usage
public class ObserverPatternDemo {
    public static void main(String[] args) {
        NewsAgency agency = new NewsAgency();
        
        // Create observers
        Observer channel1 = new NewsChannel("CNN");
        Observer channel2 = new NewsChannel("BBC");
        Observer app = new MobileApp("NewsApp");
        
        // Subscribe
        agency.attach(channel1);
        agency.attach(channel2);
        agency.attach(app);
        
        // Publish news
        agency.setNews("Breaking: Java 21 Released!");
        
        System.out.println("\nUnsubscribing BBC...\n");
        agency.detach(channel2);
        
        // Publish more news
        agency.setNews("Update: New features in Java 21 announced");
    }
}
```

### Q10: Strategy Pattern

**Answer:**

```java
// Strategy interface
interface PaymentStrategy {
    void pay(double amount);
}

// Concrete strategies
class CreditCardPayment implements PaymentStrategy {
    private String cardNumber;
    private String name;
    
    public CreditCardPayment(String cardNumber, String name) {
        this.cardNumber = cardNumber;
        this.name = name;
    }
    
    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using Credit Card: " + cardNumber);
    }
}

class PayPalPayment implements PaymentStrategy {
    private String email;
    
    public PayPalPayment(String email) {
        this.email = email;
    }
    
    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using PayPal: " + email);
    }
}

class BitcoinPayment implements PaymentStrategy {
    private String walletAddress;
    
    public BitcoinPayment(String walletAddress) {
        this.walletAddress = walletAddress;
    }
    
    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using Bitcoin: " + walletAddress);
    }
}

// Context
class ShoppingCart {
    private List<Item> items = new ArrayList<>();
    private PaymentStrategy paymentStrategy;
    
    public void addItem(Item item) {
        items.add(item);
    }
    
    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.paymentStrategy = strategy;
    }
    
    public void checkout() {
        double total = items.stream()
                           .mapToDouble(Item::getPrice)
                           .sum();
        
        System.out.println("Total amount: $" + total);
        paymentStrategy.pay(total);
    }
}

class Item {
    private String name;
    private double price;
    
    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    }
    
    public double getPrice() {
        return price;
    }
}

// Usage
public class StrategyPatternDemo {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        cart.addItem(new Item("Laptop", 1200.00));
        cart.addItem(new Item("Mouse", 25.00));
        cart.addItem(new Item("Keyboard", 75.00));
        
        // Pay with credit card
        cart.setPaymentStrategy(new CreditCardPayment("1234-5678-9012-3456", "John Doe"));
        cart.checkout();
        
        System.out.println();
        
        // Pay with PayPal
        cart.setPaymentStrategy(new PayPalPayment("john@example.com"));
        cart.checkout();
    }
}
```

---

## 🎯 Interview Questions

### When to use which pattern?

- **Singleton:** Database connections, loggers, configuration
- **Factory:** Object creation logic is complex
- **Builder:** Objects with many optional parameters
- **Observer:** Event handling, pub-sub systems
- **Strategy:** Multiple algorithms for same task
- **Decorator:** Add features dynamically
- **Adapter:** Integrate incompatible interfaces
- **Proxy:** Lazy loading, access control, logging

---

**Master these patterns for better software design!** 🚀

