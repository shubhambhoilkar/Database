//package Pack1; 
import java.util.List;
import javax.swing.Action;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver; 
import org.openqa.selenium.interactions.Actions;
public class P8_DemoAction1 {
public static void main(String[] args) {
try
{
System.setProperty("webdriver.chrome.driver",
"C:\\Users\\vishw\\Downloads\\selenium\\chrome\\chromedriver.exe");
WebDriver wd = new ChromeDriver(); 
wd.get("https://opensource-demo.orangehrmlive.com");
wd.findElement(By.id("txtUsername")).sendKeys("admin");
//locator id
name
wd.findElement(By.name("txtPassword")).sendKeys("admin123"); //locator
wd.findElement(By.className("button")).click(); //locator
class name
Actions act = new Actions(wd);
//For first level menu
act.moveToElement(wd.findElement(By.className("firstLevelMenu"))).perfo
rm();
}

catch (Exception e) {
e.printStackTrace();
}}}
