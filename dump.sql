--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Ubuntu 12.2-4)
-- Dumped by pg_dump version 12.2 (Ubuntu 12.2-4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_emailaddress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailaddress (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.account_emailaddress OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailaddress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailaddress_id_seq OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailaddress_id_seq OWNED BY public.account_emailaddress.id;


--
-- Name: account_emailconfirmation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailconfirmation (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) NOT NULL,
    email_address_id integer NOT NULL
);


ALTER TABLE public.account_emailconfirmation OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailconfirmation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailconfirmation_id_seq OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailconfirmation_id_seq OWNED BY public.account_emailconfirmation.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO postgres;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: lessons_lessonresult; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lessons_lessonresult (
    id integer NOT NULL,
    n integer NOT NULL,
    lesson_number integer NOT NULL,
    grade integer NOT NULL,
    student_id integer NOT NULL
);


ALTER TABLE public.lessons_lessonresult OWNER TO postgres;

--
-- Name: lessons_lessonresult_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lessons_lessonresult_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lessons_lessonresult_id_seq OWNER TO postgres;

--
-- Name: lessons_lessonresult_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lessons_lessonresult_id_seq OWNED BY public.lessons_lessonresult.id;


--
-- Name: lessons_taskresult; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lessons_taskresult (
    id integer NOT NULL,
    task_number integer NOT NULL,
    points integer NOT NULL,
    answer jsonb NOT NULL,
    lesson_result_id integer NOT NULL
);


ALTER TABLE public.lessons_taskresult OWNER TO postgres;

--
-- Name: lessons_taskresult_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lessons_taskresult_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lessons_taskresult_id_seq OWNER TO postgres;

--
-- Name: lessons_taskresult_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lessons_taskresult_id_seq OWNED BY public.lessons_taskresult.id;


--
-- Name: users_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_group (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    teacher_id integer NOT NULL
);


ALTER TABLE public.users_group OWNER TO postgres;

--
-- Name: users_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_group_id_seq OWNER TO postgres;

--
-- Name: users_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_group_id_seq OWNED BY public.users_group.id;


--
-- Name: users_profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_profile (
    user_id integer NOT NULL,
    dark_mode boolean NOT NULL
);


ALTER TABLE public.users_profile OWNER TO postgres;

--
-- Name: users_student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_student (
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.users_student OWNER TO postgres;

--
-- Name: users_teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_teacher (
    user_id integer NOT NULL
);


ALTER TABLE public.users_teacher OWNER TO postgres;

--
-- Name: users_unregistereduser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_unregistereduser (
    registration_code character varying(7) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    is_staff boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    group_id integer
);


ALTER TABLE public.users_unregistereduser OWNER TO postgres;

--
-- Name: account_emailaddress id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress ALTER COLUMN id SET DEFAULT nextval('public.account_emailaddress_id_seq'::regclass);


--
-- Name: account_emailconfirmation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation ALTER COLUMN id SET DEFAULT nextval('public.account_emailconfirmation_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: lessons_lessonresult id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_lessonresult ALTER COLUMN id SET DEFAULT nextval('public.lessons_lessonresult_id_seq'::regclass);


--
-- Name: lessons_taskresult id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_taskresult ALTER COLUMN id SET DEFAULT nextval('public.lessons_taskresult_id_seq'::regclass);


--
-- Name: users_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_group ALTER COLUMN id SET DEFAULT nextval('public.users_group_id_seq'::regclass);


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
1	Romez1990@yandex.ru	t	t	1
38	student38@gmail.com	t	t	38
3	teacher2@gmail.com	t	t	3
33	student33@gmail.com	t	t	33
34	student34@gmail.com	t	t	34
15	student15@gmail.com	t	t	15
26	student26@gmail.com	t	t	26
13	student13@gmail.com	t	t	13
24	student24@gmail.com	t	t	24
35	student35@gmail.com	t	t	35
22	student22@gmail.com	t	t	22
36	student36@gmail.com	t	t	36
14	student14@gmail.com	t	t	14
21	student21@gmail.com	t	t	21
32	student32@gmail.com	t	t	32
25	student25@gmail.com	t	t	25
16	student16@gmail.com	t	t	16
11	student11@gmail.com	t	t	11
31	student31@gmail.com	t	t	31
2	teacher1@gmail.com	t	t	2
37	student37@gmail.com	t	t	37
23	student23@gmail.com	t	t	23
12	student12@gmail.com	t	t	12
18	student18@gmail.com	t	t	18
17	student17@gmail.com	t	t	17
\.


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add site	7	add_site
26	Can change site	7	change_site
27	Can delete site	7	delete_site
28	Can view site	7	view_site
29	Can add Token	8	add_token
30	Can change Token	8	change_token
31	Can delete Token	8	delete_token
32	Can view Token	8	view_token
33	Can add social application	9	add_socialapp
34	Can change social application	9	change_socialapp
35	Can delete social application	9	delete_socialapp
36	Can view social application	9	view_socialapp
37	Can add social account	10	add_socialaccount
38	Can change social account	10	change_socialaccount
39	Can delete social account	10	delete_socialaccount
40	Can view social account	10	view_socialaccount
41	Can add social application token	11	add_socialtoken
42	Can change social application token	11	change_socialtoken
43	Can delete social application token	11	delete_socialtoken
44	Can view social application token	11	view_socialtoken
45	Can add email address	12	add_emailaddress
46	Can change email address	12	change_emailaddress
47	Can delete email address	12	delete_emailaddress
48	Can view email address	12	view_emailaddress
49	Can add email confirmation	13	add_emailconfirmation
50	Can change email confirmation	13	change_emailconfirmation
51	Can delete email confirmation	13	delete_emailconfirmation
52	Can view email confirmation	13	view_emailconfirmation
53	Can add profile	14	add_profile
54	Can change profile	14	change_profile
55	Can delete profile	14	delete_profile
56	Can view profile	14	view_profile
57	Can add group	15	add_group
58	Can change group	15	change_group
59	Can delete group	15	delete_group
60	Can view group	15	view_group
61	Can add student	16	add_student
62	Can change student	16	change_student
63	Can delete student	16	delete_student
64	Can view student	16	view_student
65	Can add teacher	17	add_teacher
66	Can change teacher	17	change_teacher
67	Can delete teacher	17	delete_teacher
68	Can view teacher	17	view_teacher
69	Can add unregistered user	18	add_unregistereduser
70	Can change unregistered user	18	change_unregistereduser
71	Can delete unregistered user	18	delete_unregistereduser
72	Can view unregistered user	18	view_unregistereduser
73	Can add lesson result	19	add_lessonresult
74	Can change lesson result	19	change_lessonresult
75	Can delete lesson result	19	delete_lessonresult
76	Can view lesson result	19	view_lessonresult
77	Can add task result	20	add_taskresult
78	Can change task result	20	change_taskresult
79	Can delete task result	20	delete_taskresult
80	Can view task result	20	view_taskresult
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
31	pbkdf2_sha256$180000$1Tw3svXCB61R$v6lAGoTHf2dpyMt43BrsUFcu2Q6H3R4EnvFsnhFYcBU=	2020-05-29 13:46:02.189584+03	f	student31@gmail.com	Олег	Алексеев	student31@gmail.com	f	t	2020-05-29 13:45:20.894827+03
37	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student37@gmail.com	Станислав	Антонов	student37@gmail.com	f	t	2020-05-29 13:48:54.917789+03
34	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student34@gmail.com	Фёдор	Николаев	student34@gmail.com	f	t	2020-05-29 13:48:54.917789+03
24	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-06-16 09:44:30.160812+03	f	student24@gmail.com	Владлен	Анхимов	student24@gmail.com	f	t	2020-05-29 13:48:54.917789+03
22	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student22@gmail.com	Денис	Елисеев	student22@gmail.com	f	t	2020-05-29 13:48:54.917789+03
26	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student26@gmail.com	Василий	Козлов	student26@gmail.com	f	t	2020-05-29 13:48:54.917789+03
15	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student15@gmail.com	Данил	Михайлов	student15@gmail.com	f	t	2020-05-29 13:48:54.917789+03
23	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student23@gmail.com	Леонид	Лебедев	student23@gmail.com	f	t	2020-05-29 13:48:54.917789+03
32	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student32@gmail.com	Гавриил	Королёв	student32@gmail.com	f	t	2020-05-29 13:48:54.917789+03
3	pbkdf2_sha256$180000$JvLny8ZsSrtx$63yFcIYKOYqzqOsZ7EjbD4WX13xcvZTkD491v2P+20w=	2020-06-05 06:27:37.631079+03	f	teacher2@gmail.com	Всеволод	Голубев	teacher2@gmail.com	t	t	2020-06-05 06:26:58.522481+03
16	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student16@gmail.com	Калег	Морозов	student16@gmail.com	f	t	2020-05-29 13:48:54.917789+03
12	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-06-15 18:11:24.189967+03	f	student12@gmail.com	Борис	Егоров	student12@gmail.com	f	t	2020-05-29 13:48:54.917789+03
14	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student14@gmail.com	Михаил	Зотов	student14@gmail.com	f	t	2020-05-29 13:48:54.917789+03
21	pbkdf2_sha256$180000$1Tw3svXCB61R$v6lAGoTHf2dpyMt43BrsUFcu2Q6H3R4EnvFsnhFYcBU=	2020-06-17 09:26:27.526417+03	f	student21@gmail.com	Николай	Астапов	student21@gmail.com	f	t	2020-05-29 13:45:20.894827+03
1	pbkdf2_sha256$180000$f1MYj2WD1VZJ$vPJ7KJKtZuII1moQzC8CXLtrMb+PjvTcZ7LGsEiHKpU=	2020-06-17 10:09:28.207913+03	t	Romez1990	Роман	Яковлев	Romez1990@yandex.ru	t	t	2020-05-07 11:49:07.662359+03
11	pbkdf2_sha256$180000$1Tw3svXCB61R$v6lAGoTHf2dpyMt43BrsUFcu2Q6H3R4EnvFsnhFYcBU=	2020-06-17 10:27:33.876116+03	f	student11@gmail.com	Антон	Волков	student11@gmail.com	f	t	2020-05-29 13:45:20.894827+03
25	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student25@gmail.com	Виталий	Павлов	student25@gmail.com	f	t	2020-05-29 13:48:54.917789+03
13	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student13@gmail.com	Александр	Запловин	student13@gmail.com	f	t	2020-05-29 13:48:54.917789+03
33	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student33@gmail.com	Иван	Степанов	student33@gmail.com	f	t	2020-05-29 13:48:54.917789+03
17	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student17@gmail.com	Артём	Новиков	student17@gmail.com	f	t	2020-05-29 13:48:54.917789+03
38	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student38@gmail.com	Никита	Осипов	student38@gmail.com	f	t	2020-05-29 13:48:54.917789+03
35	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student35@gmail.com	Степан	Мухин	student35@gmail.com	f	t	2020-05-29 13:48:54.917789+03
36	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-05-29 13:56:17.744817+03	f	student36@gmail.com	Матвей	Чернов	student36@gmail.com	f	t	2020-05-29 13:48:54.917789+03
18	pbkdf2_sha256$180000$62Y2HOM5T25X$QKaYk/kgEYnP4NusbAV5xZyHQSxF+63FqHscx9PpWJ4=	2020-06-15 19:24:35.783149+03	f	student18@gmail.com	Николай	Пепелыгин	student18@gmail.com	f	t	2020-05-29 13:48:54.917789+03
2	pbkdf2_sha256$180000$ky8gqEqtJ55p$2mx3BjNGU6twHTGtU3V6oBMepNip1SoLWAAoIsI95Go=	2020-06-17 10:25:53.093428+03	f	teacher1@gmail.com	Иван	Попов	teacher1@gmail.com	t	t	2020-05-30 07:26:49.84601+03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	sites	site
8	authtoken	token
9	allauth	socialapp
10	allauth	socialaccount
11	allauth	socialtoken
12	account	emailaddress
13	account	emailconfirmation
14	users	profile
15	users	group
16	users	student
17	users	teacher
18	users	unregistereduser
19	lessons	lessonresult
20	lessons	taskresult
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-06-21 13:06:53.922184+03
2	auth	0001_initial	2020-06-21 13:06:54.263869+03
3	account	0001_initial	2020-06-21 13:06:54.950121+03
4	account	0002_email_max_length	2020-06-21 13:06:55.126061+03
5	admin	0001_initial	2020-06-21 13:06:55.217572+03
6	admin	0002_logentry_remove_auto_add	2020-06-21 13:06:55.316649+03
7	admin	0003_logentry_add_action_flag_choices	2020-06-21 13:06:55.361003+03
8	contenttypes	0002_remove_content_type_name	2020-06-21 13:06:55.393113+03
9	auth	0002_alter_permission_name_max_length	2020-06-21 13:06:55.403828+03
10	auth	0003_alter_user_email_max_length	2020-06-21 13:06:55.415228+03
11	auth	0004_alter_user_username_opts	2020-06-21 13:06:55.432898+03
12	auth	0005_alter_user_last_login_null	2020-06-21 13:06:55.447468+03
13	auth	0006_require_contenttypes_0002	2020-06-21 13:06:55.450374+03
14	auth	0007_alter_validators_add_error_messages	2020-06-21 13:06:55.464681+03
15	auth	0008_alter_user_username_max_length	2020-06-21 13:06:55.545425+03
16	auth	0009_alter_user_last_name_max_length	2020-06-21 13:06:55.60505+03
17	auth	0010_alter_group_name_max_length	2020-06-21 13:06:55.630602+03
18	auth	0011_update_proxy_permissions	2020-06-21 13:06:55.643741+03
19	authtoken	0001_initial	2020-06-21 13:06:55.710461+03
20	authtoken	0002_auto_20160226_1747	2020-06-21 13:06:55.911049+03
21	users	0001_initial	2020-06-21 13:06:55.958691+03
22	users	0002_group	2020-06-21 13:06:56.04247+03
23	users	0003_student	2020-06-21 13:06:56.128166+03
24	users	0004_teacher	2020-06-21 13:06:56.256233+03
25	users	0005_unregistereduser	2020-06-21 13:06:56.329978+03
26	users	0006_auto_20200519_1624	2020-06-21 13:06:56.458272+03
27	users	0007_group_teacher	2020-06-21 13:06:56.486182+03
28	lessons	0001_initial	2020-06-21 13:06:56.692226+03
29	sessions	0001_initial	2020-06-21 13:06:56.924141+03
30	sites	0001_initial	2020-06-21 13:06:57.04452+03
31	sites	0002_alter_domain_unique	2020-06-21 13:06:57.153663+03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_site (id, domain, name) FROM stdin;
1	highm.herokuapp.com	HighM
\.


--
-- Data for Name: lessons_lessonresult; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lessons_lessonresult (id, n, lesson_number, grade, student_id) FROM stdin;
2	2	1	3	12
12	2	2	3	12
56	1	3	5	11
23	3	3	3	13
8	8	1	3	18
5	5	1	3	15
11	1	2	5	11
14	4	2	4	14
28	8	3	4	18
16	6	2	3	16
15	5	2	5	15
13	3	2	3	13
17	7	2	4	17
26	6	3	3	16
3	3	1	3	13
6	6	1	4	16
24	4	3	4	14
7	7	1	3	17
1	1	1	3	11
4	4	1	4	14
18	8	2	3	18
\.


--
-- Data for Name: lessons_taskresult; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lessons_taskresult (id, task_number, points, answer, lesson_result_id) FROM stdin;
79	1	2	{}	16
78	2	2	{}	15
81	1	2	{}	17
73	1	2	{}	13
82	2	2	{}	17
71	1	2	{}	12
77	1	3	{}	15
72	2	1	{}	12
74	2	1	{}	13
76	2	1	{}	14
69	1	3	{}	11
21	1	2	{}	1
22	2	2	{}	1
70	2	3	{}	11
75	1	3	{}	14
23	3	1	{}	1
84	2	1	{}	18
27	1	2	{}	2
28	2	2	{}	2
31	3	1	{}	2
33	1	2	{}	3
34	2	2	{}	3
37	3	1	{}	3
39	1	2	{}	4
40	2	2	{}	4
41	5	2	{}	4
43	3	1	{}	4
45	1	2	{}	5
46	2	2	{}	5
49	3	1	{}	5
51	1	2	{}	6
52	2	2	{}	6
53	5	2	{}	6
55	3	1	{}	6
57	1	2	{}	7
58	2	2	{}	7
61	3	1	{}	7
63	1	2	{}	8
64	2	2	{}	8
67	3	1	{}	8
35	5	1	{}	3
38	4	0	{}	3
36	6	1	{}	3
29	5	1	{}	2
26	6	0	{}	1
30	6	1	{}	2
32	4	0	{}	2
25	5	1	{}	1
24	4	1	{}	1
62	4	0	{}	7
59	5	1	{}	7
68	4	0	{}	8
66	6	1	{}	8
60	6	1	{}	7
47	5	1	{}	5
48	6	1	{}	5
65	5	1	{}	8
50	4	0	{}	5
80	2	1	{}	16
42	6	2	{}	4
44	4	2	{}	4
54	6	2	{}	6
56	4	2	{}	6
83	1	1	{}	18
85	1	1	{}	23
86	1	2	{}	24
87	1	1	{}	26
88	1	2	{}	28
101	1	3	{"x": 0.977913}	56
\.


--
-- Data for Name: users_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_group (id, name, created_at, teacher_id) FROM stdin;
1	admins	2020-05-07 11:23:22.801107+03	1
10	2ПрИн-5а.18	2020-05-07 13:15:16.618301+03	2
30	2СЭЗ-3.18	2020-06-05 09:42:35.238+03	3
20	2СП-2а.18	2020-06-05 09:43:58.943+03	2
16	2АЭС-6а.19	2020-06-17 10:26:37.462257+03	2
\.


--
-- Data for Name: users_profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_profile (user_id, dark_mode) FROM stdin;
1	f
2	f
3	f
11	f
12	f
13	f
14	f
15	f
16	f
17	f
18	f
21	f
22	f
23	f
24	f
25	f
26	f
31	f
32	f
33	f
34	f
35	f
36	f
37	f
38	f
\.


--
-- Data for Name: users_student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_student (user_id, group_id) FROM stdin;
1	1
35	30
16	10
17	10
18	10
34	30
12	10
13	10
14	10
15	10
24	20
25	20
26	20
11	10
21	20
22	20
23	20
33	30
32	30
38	30
37	30
36	30
31	30
\.


--
-- Data for Name: users_teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_teacher (user_id) FROM stdin;
1
2
3
\.


--
-- Data for Name: users_unregistereduser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_unregistereduser (registration_code, first_name, last_name, is_staff, created_at, group_id) FROM stdin;
c499930	Надежда Юрьевна	Шапошникова	t	2020-05-29 14:24:46.462692+03	\N
c728027	Иван	Запловин	f	2020-06-05 11:37:11.308093+03	20
c673576	Руслан	Ацаев	f	2020-06-17 10:26:37.566533+03	16
c518129	Милена	Булавинцева	f	2020-06-17 10:26:37.56662+03	16
c277008	Дмитрий	Буценко	f	2020-06-17 10:26:37.566691+03	16
c768573	Денис	Дорожков	f	2020-06-17 10:26:37.566762+03	16
c638364	Алексей	Жужгов	f	2020-06-17 10:26:37.566829+03	16
c024466	Александра	Захарова	f	2020-06-17 10:26:37.566899+03	16
c448871	Валентина	Ишкина	f	2020-06-17 10:26:37.566962+03	16
c191806	Александра	Кириллова	f	2020-06-17 10:26:37.567023+03	16
c994700	Алена	Кудрявцева	f	2020-06-17 10:26:37.56709+03	16
c883322	Иван	Куликов	f	2020-06-17 10:26:37.567167+03	16
c507087	Георгий	Мальцев	f	2020-06-17 10:26:37.567236+03	16
c786802	Валерия	Новикова	f	2020-06-17 10:26:37.5673+03	16
c688580	Никита	Сорокин	f	2020-06-17 10:26:37.567363+03	16
c756939	Максим	Чепурченко	f	2020-06-17 10:26:37.567435+03	16
c180344	Карина	Шевченко	f	2020-06-17 10:26:37.567531+03	16
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 1, false);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 80, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 20, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 31, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: lessons_lessonresult_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lessons_lessonresult_id_seq', 1, false);


--
-- Name: lessons_taskresult_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lessons_taskresult_id_seq', 1, false);


--
-- Name: users_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_group_id_seq', 1, false);


--
-- Name: account_emailaddress account_emailaddress_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_email_key UNIQUE (email);


--
-- Name: account_emailaddress account_emailaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id);


--
-- Name: account_emailconfirmation account_emailconfirmation_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_key_key UNIQUE (key);


--
-- Name: account_emailconfirmation account_emailconfirmation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: lessons_lessonresult lessons_lessonresult_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_lessonresult
    ADD CONSTRAINT lessons_lessonresult_pkey PRIMARY KEY (id);


--
-- Name: lessons_lessonresult lessons_lessonresult_student_id_lesson_number_6fa11563_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_lessonresult
    ADD CONSTRAINT lessons_lessonresult_student_id_lesson_number_6fa11563_uniq UNIQUE (student_id, lesson_number);


--
-- Name: lessons_taskresult lessons_taskresult_lesson_result_id_task_number_a933a556_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_taskresult
    ADD CONSTRAINT lessons_taskresult_lesson_result_id_task_number_a933a556_uniq UNIQUE (lesson_result_id, task_number);


--
-- Name: lessons_taskresult lessons_taskresult_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_taskresult
    ADD CONSTRAINT lessons_taskresult_pkey PRIMARY KEY (id);


--
-- Name: users_group users_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_group
    ADD CONSTRAINT users_group_name_key UNIQUE (name);


--
-- Name: users_group users_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_group
    ADD CONSTRAINT users_group_pkey PRIMARY KEY (id);


--
-- Name: users_profile users_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_pkey PRIMARY KEY (user_id);


--
-- Name: users_student users_student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_student
    ADD CONSTRAINT users_student_pkey PRIMARY KEY (user_id);


--
-- Name: users_teacher users_teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_teacher
    ADD CONSTRAINT users_teacher_pkey PRIMARY KEY (user_id);


--
-- Name: users_unregistereduser users_unregistereduser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_unregistereduser
    ADD CONSTRAINT users_unregistereduser_pkey PRIMARY KEY (registration_code);


--
-- Name: account_emailaddress_email_03be32b2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_email_03be32b2_like ON public.account_emailaddress USING btree (email varchar_pattern_ops);


--
-- Name: account_emailaddress_user_id_2c513194; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_user_id_2c513194 ON public.account_emailaddress USING btree (user_id);


--
-- Name: account_emailconfirmation_email_address_id_5b7f8c58; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_email_address_id_5b7f8c58 ON public.account_emailconfirmation USING btree (email_address_id);


--
-- Name: account_emailconfirmation_key_f43612bd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_key_f43612bd_like ON public.account_emailconfirmation USING btree (key varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: lessons_lessonresult_student_id_bc15b628; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX lessons_lessonresult_student_id_bc15b628 ON public.lessons_lessonresult USING btree (student_id);


--
-- Name: lessons_taskresult_lesson_result_id_8993a748; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX lessons_taskresult_lesson_result_id_8993a748 ON public.lessons_taskresult USING btree (lesson_result_id);


--
-- Name: users_group_name_5f613b12_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_group_name_5f613b12_like ON public.users_group USING btree (name varchar_pattern_ops);


--
-- Name: users_group_teacher_id_f075691c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_group_teacher_id_f075691c ON public.users_group USING btree (teacher_id);


--
-- Name: users_student_group_id_baa0cf83; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_student_group_id_baa0cf83 ON public.users_student USING btree (group_id);


--
-- Name: users_unregistereduser_code_996a77a5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_unregistereduser_code_996a77a5_like ON public.users_unregistereduser USING btree (registration_code varchar_pattern_ops);


--
-- Name: users_unregistereduser_group_id_dae4b9e7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_unregistereduser_group_id_dae4b9e7 ON public.users_unregistereduser USING btree (group_id);


--
-- Name: account_emailaddress account_emailaddress_user_id_2c513194_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_2c513194_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emailconfirmation account_emailconfirm_email_address_id_5b7f8c58_fk_account_e; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirm_email_address_id_5b7f8c58_fk_account_e FOREIGN KEY (email_address_id) REFERENCES public.account_emailaddress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lessons_lessonresult lessons_lessonresult_student_id_bc15b628_fk_users_stu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_lessonresult
    ADD CONSTRAINT lessons_lessonresult_student_id_bc15b628_fk_users_stu FOREIGN KEY (student_id) REFERENCES public.users_student(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lessons_taskresult lessons_taskresult_lesson_result_id_8993a748_fk_lessons_l; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lessons_taskresult
    ADD CONSTRAINT lessons_taskresult_lesson_result_id_8993a748_fk_lessons_l FOREIGN KEY (lesson_result_id) REFERENCES public.lessons_lessonresult(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_group users_group_teacher_id_f075691c_fk_users_teacher_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_group
    ADD CONSTRAINT users_group_teacher_id_f075691c_fk_users_teacher_user_id FOREIGN KEY (teacher_id) REFERENCES public.users_teacher(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_profile users_profile_user_id_2112e78d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_user_id_2112e78d_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_student users_student_group_id_baa0cf83_fk_users_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_student
    ADD CONSTRAINT users_student_group_id_baa0cf83_fk_users_group_id FOREIGN KEY (group_id) REFERENCES public.users_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_student users_student_user_id_dc59cd64_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_student
    ADD CONSTRAINT users_student_user_id_dc59cd64_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_teacher users_teacher_user_id_bc9e1389_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_teacher
    ADD CONSTRAINT users_teacher_user_id_bc9e1389_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_unregistereduser users_unregistereduser_group_id_dae4b9e7_fk_users_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_unregistereduser
    ADD CONSTRAINT users_unregistereduser_group_id_dae4b9e7_fk_users_group_id FOREIGN KEY (group_id) REFERENCES public.users_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

