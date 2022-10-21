def create_trigger_payload(self, message):
        payload = {
            'msg': message.text.encode('ascii', 'ignore'),
            'user': message.sender_screen_name.encode('ascii', 'ignore'),
            # Cast to string to mitigate long integer bug in product
            'id': str(message.id),
            'created_at': message.created_at.encode('ascii', 'ignore'),
            'sender_id': message.sender_id,
            'sender_created_at': message.sender.created_at.encode('ascii', 'ignore'),
            'sender_default_profile': message.sender.default_profile,
            'sender_default_profile_image': message.sender.default_profile_image,
            'sender_description': message.sender.description.encode('ascii', 'ignore'),
            'sender_followers_count': message.sender.followers_count,
            'sender_friends_count': message.sender.friends_count,
            'sender_lang': message.sender.lang.encode('ascii', 'ignore'),
            'sender_location': message.sender.location.encode('ascii', 'ignore'),
            'sender_name': message.sender.name.encode('ascii', 'ignore'),
            'recipient_id': message.recipient_id
        }
        self.logger.info("Create Trigger Payload: Created {payload}".format(payload=payload))
        return payload 
create_trigger_payload()