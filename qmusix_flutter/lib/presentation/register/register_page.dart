import 'package:flutter/material.dart';
import 'package:qmusix/domain/repository/auth_repository.dart';
import 'package:qmusix/injection.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Register Page"),
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
                AppInjection.get<AuthRepository>().register(
                  username: _usernameController.text,
                  password: _passwordController.text,
                );
              },
              child: const Text("Register"),
            ),
          ],
        ),
      ),
    );
  }
}
