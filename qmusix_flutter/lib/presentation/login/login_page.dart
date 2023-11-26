import 'package:flutter/material.dart';
import 'package:qmusix/domain/repository/auth_repository.dart';
import 'package:qmusix/injection.dart';
import 'package:qmusix/presentation/authenticate/widgets/app_textfield.dart';

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
        child: Container(
          decoration: BoxDecoration(
            color: Colors.grey[300],
            borderRadius: BorderRadius.circular(8),
          ),
          width: MediaQuery.of(context).size.width * 0.5,
          height: MediaQuery.of(context).size.width * 0.5,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisSize: MainAxisSize.min,
            children: [
              AppTextField(
                controller: _usernameController,
                hintText: "Username",
              ),
              AppTextField.password(
                controller: _passwordController,
                hintText: "Password",
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
      ),
    );
  }
}
