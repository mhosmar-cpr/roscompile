PYTHON_REPLACEMENTS = {
    r'import\ rospy': 'import rclpy\nfrom rclpy.node import Node',
    r'\n(\s+)rospy.init_node\((.*)\)': '\n$0rclpy.init(args=args)\n$0node = ClassName($1)\n$0rclpy.spin(node)\n$0node.destroy_node()\n$0rclpy.shutdown()',
    r'\n(\s+)__init__\(self\):': '$0__init__(self, name):$0    super().__init__(name)',
    r'class\s+(\w*):': 'class $0(Node):',
    r'rospy.Publisher\(([^\,]+), ([^\)]+)\)': 'self.create_publisher($1, $0, 10)',
    r'rospy.Subscriber\(([^\,]+), ([^\,]+), ([^\)]+)\)': 'self.create_subscription($1, $0, $2, 10)',
    r'rospy.Service\(([^\,]+), ([^\,]+), ([^\)]+)\)': 'self.create_service($1, $0, $2)',
    r'rospy\.get_param\(([^\,\n]+),[\ \t]*([^\s]+)\)': 'self.declare_parameter($0, $1).value',
    r'rospy\.get_param\(([^\s]+)\)': 'self.declare_parameter($0, rclpy.Parameter.Type.DOUBLE).value',
    r'rospy\.logdebug\((.+)\)': 'self.get_logger().debug($0)',
    r'rospy\.loginfo\((.+)\)': 'self.get_logger().info($0)',
    r'rospy\.logwarn\((.+)\)': 'self.get_logger().warning($0)',
    r'rospy\.logerr\((.+)\)': 'self.get_logger().error($0)',
    r'rospy\.logfatal\((.+)\)': 'self.get_logger().fatal($0)',
    r'rospy\.Duration\(([^\s]+)\)': 'rclpy.duration.Duration($0)',
    r'rospy\.Time\.now\(\)': 'self.get_clock().now()',
    r'rospy\.Time\(0\)': 'rclpy.time.Time()',
    r'rospy\.is_shutdown\(\)': 'not rclpy.ok()',
    r'rospy\.Rate\(([^\s]+)\)': 'self.create_rate($0)',
}


def update_python(package):
    package.source_code.modify_with_patterns(PYTHON_REPLACEMENTS, language='python')
