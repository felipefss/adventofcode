import 'dart:io';

void main() async {
  File file = File('example.txt');
  List<String> input = await file.readAsLines();

  // Build directory tree
  var tree = {'/': Map<String, dynamic>()};
  List<String> cwd = ['/'];

  for (final line in input) {
    if (line.startsWith('\$')) {
      var cmdList = line.split(' ');
      var cmd = cmdList[1];

      if (cmd == 'cd') {
        var arg = cmdList[2];
      }
      if (cmd == 'ls') {}
    }
  }
}
