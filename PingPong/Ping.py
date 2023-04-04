import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Ping(Node):

    def __init__(self):
        super().__init__("Ping")
        self.publisher = self.create_publisher(String, 'pingpong', 10)
        self.subscription = self.create_subscription(
            String,
            'pongping',
            self.ping_callback,
            10)

    def ping_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        msg = String()
        msg.data = 'Ping' 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
        rclpy.init(args=args)
        node = Ping()
        rclpy.spin(node)
        rclpy.shutdown()


if __name__ == '__main__':
    main()
