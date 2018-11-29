package PCproblem;

public class Test {
    private static Integer count = 0; //产品计数
    private static final Integer FULL = 1; //最多产品数量
    private static String LOCK = "lock"; //产品加锁
    public static void main(String[] args) {
        Test test1 = new Test();
        Thread xiaoMing = new Thread(test1.new Producer());
        xiaoMing.setName("小明同学");
        Thread xiaoHua = new Thread(test1.new Consumer());
        xiaoHua.setName("小花同学");
        Thread xiaoHong = new Thread(test1.new Consumer());
        xiaoHong.setName("小红同学");
        Thread xiaolan = new Thread(test1.new Consumer());
        xiaolan.setName("小兰同学");
        xiaoMing.start();
        xiaoHong.start();
        xiaoHua.start();
        xiaolan.start();
    }
    class Producer implements Runnable {
        @Override
        public void run() {
            while (true){
                try {
                    Thread.sleep(1000);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                synchronized (LOCK) {//只允许生产者操作产品
                    while (count == FULL) {//生产满了
                        try {
                            System.out.println("烤箱满了，" + Thread.currentThread().getName()  + "要休息一会了");
                            LOCK.wait();//生产者进程挂起
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                    count++;
                    System.out.println(Thread.currentThread().getName() + "做了一个香喷喷的面包，目前总共有" + count + "个面包");
                    LOCK.notifyAll();//唤醒其他等待的进程
                }
            }
        }
    }
    class Consumer implements Runnable {
        @Override
        public void run() {
            while (true){
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                synchronized (LOCK) {
                    while (count == 0) {
                        try {
                            System.out.println("哎呀！面包吃完了" + Thread.currentThread().getName()  + "要等一会");
                            LOCK.wait();
                        } catch (Exception e) {
                        }
                    }
                    count--;
                    System.out.println(Thread.currentThread().getName() + "吃了一个面包，目前总共有" + count + "个面包");
                    LOCK.notifyAll();
                }
            }
        }
    }
}
