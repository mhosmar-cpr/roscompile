PYTHON_REPLACEMENTS = {
    r'\n(\s+)rospy.init_node\((.*)\)': '\n$0rclpy.init(args=args)\n$0node = ClassName($1)\n$0rclpy.spin(node)\n$0node.destroy_node()\n$0rclpy.shutdown()',
    r'rospy.Publisher\(([^\,]+), ([^\)]+)\)': 'self.create_publisher($1, $0)',
    r'rospy.Subscriber\(([^\,]+), ([^\,]+), ([^\)]+)\)': 'self.create_subscription($1, $0, $2)',
    r'rospy.Service\(([^\,]+), ([^\,]+), ([^\)]+)\)': 'self.create_service($1, $0, $2)',
    r'\n(\s+)([^\s]+)[\ \t]*=[\ \t]*rospy\.get_param\(([^\,\n]+),[\ \t]*([^\s]+)\)': '\n$0$1 = self.declare_parameter($2, $3).value',
    r'\n(\s+)([^\s]+)[\ \t]*=[\ \t]*rospy\.get_param\(([^\s]+)\)': '\n$0$1 = self.declare_parameter($2, rclpy.Parameter.Type.DOUBLE).value',
    r'\n(\s+)rospy\.logdebug\(([^\s]+)\)': '\n$0self.get_logger().debug($1)',
    r'\n(\s+)rospy\.loginfo\(([^\s]+)\)': '\n$0self.get_logger().info($1)',
    r'\n(\s+)rospy\.logwarn\(([^\s]+)\)': '\n$0self.get_logger().warning($1)',
    r'\n(\s+)rospy\.logerr\(([^\s]+)\)': '\n$0self.get_logger().error($1)',
    r'\n(\s+)rospy\.logfatal\(([^\s]+)\)': '\n$0self.get_logger().fatal($1)',
    r'\n(\s+)rospy\.Duration\(([^\s]+)\)': '\n$0rclpy.duration.Duration($1)',
    r'\n(\s+)rospy\.Time\.now\(\)': '\n$0self.get_clock().now()',
    r'\n(\s+)rospy\.is_shutdown\(\)': '\n$0rclpy.ok()',
    r'\n(\s+)rospy\.Rate\(([^\s]+)\)': '\n$0self.create_rate($1)',
}


def update_python(package):
    package.source_code.modify_with_patterns(PYTHON_REPLACEMENTS, language='python')
