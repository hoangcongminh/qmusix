import 'package:flutter/material.dart';
import 'package:qmusix/domain/repository/auth_repository.dart';
import 'package:qmusix/injection.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Login Page"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            TextFormField(
              controller: _usernameController,
              decoration: const InputDecoration(
                labelText: "Username",
              ),
            ),
            TextFormField(
              controller: _passwordController,
              obscureText: true,
              decoration: const InputDecoration(
                labelText: "Password",
              ),
            ),
            FilledButton(
              onPressed: () {
                // context.push("/home");
                AppInjection.get<AuthRepository>().login(
                  username: _usernameController.text,
                  password: _passwordController.text,
                );
              },
              child: const Text("Login"),
            ),
          ],
        ),
      ),
    );
  }
}
