public class Cleaner
{
    public Action Do(Location location, State state)
    {
        return state == State.Dirty ? Action.Clear : location == Location.A ? Action.MoveRight : Action.MoveLeft;
    }
}

public enum Location
{
    A = 0,
    B = 1,
}

public enum State
{
    Clean = 0,
    Dirty = 1,
}

public enum Action
{
    Clear = 0,
    MoveRight = 1,
    MoveLeft = 2
}

