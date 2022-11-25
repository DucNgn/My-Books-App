import { IUserProfile, IBookInfo, IShelvesStorage } from '@/interfaces';

export interface AppNotification {
  content: string;
  color?: string;
  showProgress?: boolean;
}

export interface MainState {
  token: string;
  isLoggedIn: boolean | null;
  logInError: boolean;
  userProfile: IUserProfile | null;
  dashboardMiniDrawer: boolean;
  dashboardShowDrawer: boolean;
  notifications: AppNotification[];
  currentBook: IBookInfo | null;
  personalShelves: IShelvesStorage | null;
}
