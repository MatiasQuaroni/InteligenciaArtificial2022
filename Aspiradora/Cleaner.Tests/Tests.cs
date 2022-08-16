using System.ComponentModel.DataAnnotations;
using Xunit;

namespace Aspiradora.Tests;

public class Tests
{
    private readonly Cleaner _cleaner = new Cleaner();
    
    [Fact]
    public void Hoover_IfDirty_ShouldClean()
    {
        var result = this._cleaner.Do(Location.A, State.Dirty);
        Assert.True(result == Action.Clear);
    }

    [Fact]
    public void Hoover_IfClean_AndLocationA_ShouldMoveRight()
    {
        var result = this._cleaner.Do(Location.A, State.Clean);
        Assert.True(result == Action.MoveRight);
    }

    [Fact]
    public void Hoover_IfClean_AndLocationB_ShouldMoveLeft()
    {
        var result = this._cleaner.Do(Location.B, State.Clean);
        Assert.True(result == Action.MoveLeft);
    }
}