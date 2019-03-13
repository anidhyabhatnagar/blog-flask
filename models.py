# The models.py specifies the model for the blog entries

import datetime, re
from app import db


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()

# Following we are creating 'entry_tags' table which establishes a link
# between the Entry and Tag models. Then in Entry class we will use
# db.relationship function of SQLAlchemy which provides high-level API for
# working with this relationship.
entry_tags = db.Table('entry_tags',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
        db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'))
    )

# The following class Entry is the model for blog entries.
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_timestamp = db.Column(
            db.DateTime,
            default=datetime.datetime.now,
            onupdate=datetime.datetime.now)

    # The db.relationship function creates a new property on the Entry model
    # that allows us to easily read and write the tags for a given blog entry.
    #
    # The first two arguments, 'Tag' and secondary=entry_tags, instruct
    # SQLAlchemy that we are going to be querying the Tag model via the
    # entry_tags table.
    #
    # The third argument creates a back-reference, allowing us to go from the
    # Tag model back to the associated list of blog entries. By specifying
    # lazy='dynamic', we instruct SQLAlchemy that, instead of it loading all
    # the associated entries for us, we want a Query object instead.
    tags = db.relationship('Tag', secondary=entry_tags,
            backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)
    
    def __repr__(self):
        return '<Entry: %s>' % self.title

# The following class Tag is the model for tags.
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64), unique=True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag %s>' % self.name


