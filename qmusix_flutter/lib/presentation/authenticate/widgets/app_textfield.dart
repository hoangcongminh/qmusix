import 'package:flutter/material.dart';

class AppTextField extends StatelessWidget {
  final TextEditingController? controller;
  final String? hintText;
  final bool? obscureText;

  const AppTextField({
    super.key,
    this.controller,
    this.hintText,
    this.obscureText,
  });

  const AppTextField.password({
    super.key,
    this.controller,
    this.hintText,
  }) : obscureText = true;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: TextFormField(
        controller: controller,
        obscureText: obscureText ?? false,
        decoration: InputDecoration(
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          hintText: hintText,
        ),
      ),
    );
  }
}
