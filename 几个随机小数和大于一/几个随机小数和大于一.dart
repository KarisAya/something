// 计算结果 2.7183122 计算耗时 0.474 秒
import 'dart:math';

const LOOP = 10000000;
void main() {
  var random = Random(DateTime.now().millisecondsSinceEpoch);
  var stopwatch = Stopwatch()..start();
  int n = 0;
  for (int _ = 0; _ < LOOP; ++_)
    for (double x = 0.0; x < 1; x += random.nextDouble()) ++n;
  stopwatch.stop();
  print('计算结果 ${n / LOOP} 计算耗时 ${stopwatch.elapsedMilliseconds / 1000} 秒');
}
