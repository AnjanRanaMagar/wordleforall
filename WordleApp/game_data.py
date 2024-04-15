from WordleApp import db
from WordleApp.models import User, Score
from datetime import datetime
from flask_login import current_user

def add_score(score_value, attempts_count,time_needed):
    if not current_user.is_authenticated:
        return None 
    new_score = Score(user_id=current_user.id, score=score_value, attempts=attempts_count, time_taken=time_needed)
    db.session.add(new_score)
    db.session.commit()
    return new_score


def get_scores(user_id=None):
    query = Score.query.join(User, user_id== Score.user_id)
    if user_id:
        query = query.filter(Score.user_id == user_id)
    query = query.order_by(Score.date.asc())
    
    scores_with_users = query.all()
    return scores_with_users

