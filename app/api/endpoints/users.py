from fastapi import APIRouter, HTTPException, Depends
from ..database_utils import get_db
from ...schemas import UserCreate, UserRead
import bcrypt

router = APIRouter()






@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, cursor=Depends(get_db)):
    # Überprüfen, ob der Benutzername bereits existiert
    cursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
    existing_user = cursor.fetchone()
    if existing_user:
        raise HTTPException(status_code=400, detail="Benutzername bereits vergeben.")
    
    # Benutzer hinzufügen, wenn nicht vorhanden
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    sql = "INSERT INTO users (username, email, hashed_password, is_active) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (user.username, user.email, hashed_password, user.is_active))
    user_id = cursor.lastrowid
    return {"id": user_id, "username": user.username, "email": user.email, "is_active": user.is_active}
    


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, cursor=Depends(get_db)):
    cursor.execute("SELECT id, username, email, is_active FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[UserRead])
def read_all_users(cursor=Depends(get_db)):
    cursor.execute("SELECT id, username, email, is_active FROM users")
    users = cursor.fetchall()
    return users


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, cursor=Depends(get_db)):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    affected_rows = cursor.rowcount
    cursor.connection.commit()
    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


  