# 进程和线程的对比的是哪个方向

# 1. 关系对比
# 2. 区别对比
# 3. 优缺点对比


# 关系对比

# 1. 线程是依附在进程里面的，没有进程就没有线程

# 2. 一个进程默认提供一条线程，进程可以创建对个线程。

# 区别对待

# 1. 进程之间不共享全局变量

# 2. 线程之间共享全局变量

# 3. 创建进程的资源开销要比创建线程的资源开销要大

# 4. 线程不能独立运行，必须 依存在进程中

# 5. 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位

# 6. 多进程开发要比单进程多线程稳定性要强


# 优缺点对比

# 进程优缺点：
# 优点：可以用多核
# 缺点：资源开销大

# 线程优缺点：
# 优点：资源开销小
# 缺点： 不能使用多核

# 小结：
# 进程和线程都是完成多任务的一种方式
# 多进程要比多进程消耗的资源多，但是多进程开发比单进程多线程开发稳定性强，某个进程挂掉不会影响其他进程
# 多进程可以使用cpu的多核运行，多线程可以共享全局变量

# 线程不能单独执行必须依附在进程里面