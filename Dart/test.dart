import 'dart:io';
import 'dart:math';

class Point {
  final num x;
  final num y;
  final num distanceFromOrigin;

  Point(x, y)
      : x = x,
        y = y,
        distanceFromOrigin = sqrt(x*x + y*y);
}

main() {
  var p = new Point(2, 2);
  print('This is something: ${p.distanceFromOrigin}');
}


/* void main() {

  var callbacks = [];
  for (var i = 0; i < 10; i++){
    callbacks.add(()=>print(i));
  }
  callbacks.forEach((c) => c());
} */
