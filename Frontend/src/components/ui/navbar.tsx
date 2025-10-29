import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { KanbanSquare, User, Settings, LogOut, Plus } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";

interface NavbarProps {
  user?: {
    name: string;
    email: string;
    avatar?: string;
  };
}

export function Navbar({ user }: NavbarProps) {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Handle logout logic here
    navigate("/");
  };

  return (
    <nav className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link to={user ? "/dashboard" : "/"} className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center">
              <KanbanSquare className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold text-foreground">TaskFlow</span>
          </Link>

          {/* Navigation */}
          <div className="flex items-center space-x-4">
            {user ? (
              <>
                <Button variant="ghost" asChild>
                  <Link to="/dashboard">Dashboard</Link>
                </Button>
                <Button variant="ghost" asChild>
                  <Link to="/projects">Projects</Link>
                </Button>
                <Button variant="hero" size="sm" asChild>
                  <Link to="/projects/new">
                    <Plus className="w-4 h-4 mr-2" />
                    New Project
                  </Link>
                </Button>
                
                {/* User Menu */}
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <Button variant="ghost" className="relative h-8 w-8 rounded-full">
                      <Avatar className="h-8 w-8">
                        <AvatarImage src={user.avatar} alt={user.name} />
                        <AvatarFallback>{user.name.slice(0, 2).toUpperCase()}</AvatarFallback>
                      </Avatar>
                    </Button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent className="w-56" align="end" forceMount>
                    <DropdownMenuItem asChild>
                      <Link to="/profile" className="cursor-pointer">
                        <User className="mr-2 h-4 w-4" />
                        Profile
                      </Link>
                    </DropdownMenuItem>
                    <DropdownMenuItem asChild>
                      <Link to="/settings" className="cursor-pointer">
                        <Settings className="mr-2 h-4 w-4" />
                        Settings
                      </Link>
                    </DropdownMenuItem>
                    <DropdownMenuItem onClick={handleLogout} className="cursor-pointer">
                      <LogOut className="mr-2 h-4 w-4" />
                      Log out
                    </DropdownMenuItem>
                  </DropdownMenuContent>
                </DropdownMenu>
              </>
            ) : (
              <>
                <Button variant="ghost" asChild>
                  <Link to="/login">Sign In</Link>
                </Button>
                <Button variant="hero" asChild>
                  <Link to="/register">Get Started</Link>
                </Button>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}