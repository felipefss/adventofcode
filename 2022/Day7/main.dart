import 'dart:io';

List getDirRef(Map tree, String dir) {
  if (tree.containsKey(dir)) {
    return [tree[dir], true];
  }

  var result = [];
  for (final k in tree.keys) {
    if (tree[k] is Map) {
      result = getDirRef(tree[k], dir);

      if (result[1]) {
        return result;
      }
    }
  }

  return [result, false];
}

void main() async {
  File inputFile = File('example.txt');
  List<String> input = await inputFile.readAsLines();

  // Build directory tree
  var tree = {'/': Map<String, dynamic>()};
  List<String> cwd = ['/'];

  for (final line in input) {
    // Treat commands
    if (line.startsWith('\$')) {
      var cmdList = line.split(' ');
      var cmd = cmdList[1];

      if (cmd == 'cd') {
        var arg = cmdList[2];

        switch (arg) {
          case '/':
            cwd = cwd.sublist(0, 1);
            break;
          case '..':
            cwd.removeLast();
            break;
          default:
            cwd.add(arg);
        }
      }
    } else {
      // Treat files/dirs
      var fileInfo = line.split(' ');

      // Get ref to current dir
      Map currentRef = getDirRef(tree, cwd.last)[0];
      if (fileInfo[0] == 'dir') {
        currentRef[fileInfo[1]] = {};
      } else {
        currentRef[fileInfo[1]] = fileInfo[0];
      }
    }
  }

  // Part 1
}
