// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'change_password_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ChangePasswordParam _$ChangePasswordParamFromJson(Map<String, dynamic> json) =>
    ChangePasswordParam(
      userName: json['user_name'] as String,
      oldPassword: json['old_password'] as String,
      newPassword: json['new_password'] as String,
    );

Map<String, dynamic> _$ChangePasswordParamToJson(
        ChangePasswordParam instance) =>
    <String, dynamic>{
      'user_name': instance.userName,
      'old_password': instance.oldPassword,
      'new_password': instance.newPassword,
    };
