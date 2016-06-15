TABLE_PREFIX = "phpbb_"

def create_forums(forumList):
    left = 4
    with open("forums.sql", "w+") as file:
        for key, val in forumList.items():
            file.write(
                'INSERT INTO ' + TABLE_PREFIX + 'forums (forum_id, parent_id, left_id, right_id, forum_name, forum_desc, forum_type) VALUES (%i, %i, %i, %i, \'%s\', \'%s\', %i);\n' % ((int(val.id), 1, left, left+1, val.name, "", 1)))
            left += 2