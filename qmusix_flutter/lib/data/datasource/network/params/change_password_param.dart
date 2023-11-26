import 'package:json_annotation/json_annotation.dart';

part 'change_password_param.g.dart';

@JsonSerializable(fieldRename: FieldRename.snake)
class ChangePasswordParam {
  final String? userName;
  final String? oldPassword;
  final String? newPassword;

  ChangePasswordParam({
    this.userName,
    this.oldPassword,
    this.newPassword,
  });

  factory ChangePasswordParam.fromJson(Map<String, dynamic> json) =>
      _$ChangePasswordParamFromJson(json);

  Map<String, dynamic> toJson() => _$ChangePasswordParamToJson(this);
}
