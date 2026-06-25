import { Link } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'
import AuthForm from '../components/auth/AuthForm'

export default function LoginPage() {
  const { signIn } = useAuth()

  const handleLogin = async (email: string, password: string) => {
    await signIn(email, password)
  }

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>Omni Biosystems</h1>
        <p style={styles.subtitle}>Sign in to your account</p>
        <AuthForm mode="login" onSubmit={handleLogin} />
        <p style={styles.footer}>
          Don't have an account? <Link to="/register">Register</Link>
        </p>
      </div>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  page: { minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--color-bg)' },
  card: { background: 'var(--color-surface)', borderRadius: 'var(--radius)', border: '1px solid var(--color-border)', padding: '2.5rem', width: '100%', maxWidth: '400px', boxShadow: 'var(--shadow)', display: 'flex', flexDirection: 'column', gap: '1.25rem' },
  title: { fontSize: '1.5rem', fontWeight: 700, textAlign: 'center' },
  subtitle: { color: 'var(--color-muted)', textAlign: 'center', fontSize: '0.9rem' },
  footer: { textAlign: 'center', fontSize: '0.875rem', color: 'var(--color-muted)' },
}
