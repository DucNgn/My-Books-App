export interface IUserProfile {
    favorite_genres: string[]
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}


export interface IShelvesStorage {
    id: string;
    reading_shelf: IBookInfo[];
    toread_shelf: IBookInfo[];
    read_shelf: IBookInfo[];
    favorite_shelf: IBookInfo[];
    recommendation_shelf: IBookInfo[]
}

export interface IBookInfo {
    id: string;
    title: string;
    author: string;
    genre: string;
    isbn: Number;
    publication_year: Number;
    cover_image_url: string;
    num_of_pages: Number;
}