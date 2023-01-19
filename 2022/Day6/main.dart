import 'dart:io';

int getStartOfMarker(String str, int msgSize) {
  int limit = msgSize - 1;

  for (int i = limit; i < str.length; i++) {
    var chars = str.substring(i - limit, i + 1).split('');
    final charSet = chars.toSet();

    if (charSet.length == msgSize) {
      return (i + 1);
    }
  }

  return 0;
}

void main() async {
  File input = File('input.txt');

  String buffer = await input.readAsString();

  // Part 1
  // print(getStartOfMarker(buffer, 4));

  // Part 2
  print(getStartOfMarker(buffer, 14));
}
