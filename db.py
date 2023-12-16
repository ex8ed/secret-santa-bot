# -*- coding: UTF-8 -*-
import sqlite3


class Database:
    """Database-provider class"""

    def __init__(self, db_path):
        self.connection = sqlite3.Connection(db_path)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            return bool(len(result))

    def set_vk_id(self, user_id, vk_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `vk_id` = ? WHERE `user_id` = ?",
                                       (vk_id, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?",
                                         (user_id,))
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id = ?`",
                                       (signup, user_id,))

    # TODO: Provide operations for sending track number
    def set_track_number(self, user_id, tracker):
        ...

    def get_track_number(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `track_number` FROM `users` WHERE `user_id` = ?",
                                         (user_id,))
            for row in result:
                tracker = str(row[0])
            return tracker
