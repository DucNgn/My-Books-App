import { IUserProfile } from '@/interfaces';

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
    currentBook: BookInfo | null;
}

export interface BookInfo {
    id: string;
    title: string;
    author: string;
    genre: string;
    isbn: Number;
    cover_image_url: string;
    num_of_pages: Number;
}