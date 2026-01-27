import 'dart:convert';
import 'package:http/http.dart' as http;

Future<void> fetchPosts() async {
  final url = Uri.parse('http://127.0.0.1:8000/api/posts/');

  final response = await http.get(url);

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    print(data);
  } else {
    print('Failed: ${response.statusCode}');
  }
}

void main() {
  fetchPosts();
}
